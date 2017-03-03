# --*-- coding: utf-8 --*--
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from bestbuynow.views import custom_proc
from xml.dom import minidom
from bestbuynow import settings
from PIL import Image
from models import *
from board.models import *
from board.views import add_br
from forms import *
import lxml.html as html
import urllib2
import socket


@csrf_exempt
def reg_company(request, id_user):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	company_form = CompanyForm(request.POST)
	if request.method == "POST" and company_form.is_valid():
		categories = request.POST.getlist("category", "")
		status = Status.objects.get(name = "На проверке")
		company = request.POST.get("company", "")
		address = request.POST.get("address", "")
		metro = request.POST.get("metro", "")
		phone = request.POST.get("phone", "")
		fax = request.POST.get("fax", "")
		icq = request.POST.get("icq", "")
		website = request.POST.get("website", "")
		email = request.POST.get("email", "")
		opening_times = request.POST.get("opening_times", "")
		description = add_br(request.POST.get("description", ""))
		logo = request.FILES.get("logo", "")
		user_company = UserCompany(user_account = user, city = user.city, status = status, 
								   company = company, address = address, metro = metro, phone = phone, fax = fax, 
								   icq = icq, website = website, email = email, opening_times = opening_times,
								   description = description, logo = logo)
		user_company.save()
		if user_company.logo:
			img = Image.open(settings.MEDIA_ROOT + "/{0}".format(user_company.logo))
			img.thumbnail((200, 200), Image.ANTIALIAS)
			img.save(settings.MEDIA_ROOT + "/{0}".format(user_company.logo))
		for category in categories:
			user_company.categories.add(category)
		result = True
	return render_to_response("base_reg_company.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
def catalog_index (request):
	categories = CategoryCompany.objects.order_by("name")
	if 'search' in request.GET and request.GET['search']:
		search = request.GET.get("search", "")
		company = UserCompany.objects.filter(company__icontains = search)
		if not company:
			not_company = True
		paginator = Paginator(company, 15)
		page = request.GET.get('page')
		try:
			list_company = paginator.page(page)
		except PageNotAnInteger:
			list_company  = paginator.page(1)
		except EmptyPage:
			list_company  = paginator.page(paginator.num_pages)
		return render_to_response("base_company.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	return render_to_response("base_catalog_index.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
def all_company (request, id_cath):
	try:
		category = CategoryCompany.objects.get(id = id_cath)
	except CategoryCompany.DoesNotExist:
		raise Http404
	status = Status.objects.get(name = "Одобрено")	
	company = UserCompany.objects.filter(categories = category, status = status).order_by('-id')
	paginator = Paginator(company, 15)
	page = request.GET.get('page')
	try:
		list_company = paginator.page(page)
	except PageNotAnInteger:
		list_company  = paginator.page(1)
	except EmptyPage:
		list_company  = paginator.page(paginator.num_pages)
	return render_to_response("base_company.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
	
def page_firm (request, id_company):
	try:
		company = UserCompany.objects.select_related("user").get(id = id_company)
	except UserCompany.DoesNotExist:
		raise Http404
	return render_to_response("base_page_firm.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
	
def user_firms (request, id_user):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	company_list = UserCompany.objects.filter(user_account = user)
	if "delcompany" in request.GET and request.GET['delcompany']:
		company = UserCompany.objects.get(id = request.GET.get('delcompany', ''))
		company.delete()
		return HttpResponseRedirect("/catalog/firms/{0}".format(user.id))
	return render_to_response("base_user_firms.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	

@csrf_exempt
def change_firm (request, id_user, change_company):
	list_option = []
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	company = UserCompany.objects.get(id = change_company)
	category_list = CategoryCompany.objects.all()
	for category in category_list:
		if category in company.categories.all():
			list_option.append("<option selected='{0}' value='{1}'>{2}</option>".format(category, category.id, category) )
		else:
			list_option.append("<option value='{0}'>{1}</option>".format(category.id, category) )
	if request.method == "POST":
		categories = request.POST.getlist("category", "")
		city = request.POST.get("city", "")
		status = Status.objects.get(name = "На проверке")
		change_firm = request.POST.get("company", "")
		address = request.POST.get("address", "")
		metro = request.POST.get("metro", "")
		phone = request.POST.get("phone", "")
		fax = request.POST.get("fax", "")
		icq = request.POST.get("icq", "")
		website = request.POST.get("website", "")
		email = request.POST.get("email", "")
		opening_times = request.POST.get("opening_times", "")
		description = request.POST.get("description", "")
		logo = request.FILES.get("logo", "")
		UserCompany.objects.filter(id = change_company).update(user_account = user, city = city, status = status, 
								   company = change_firm, address = address, metro = metro, phone = phone, fax = fax, 
								   icq = icq, website = website, email = email, opening_times = opening_times,
								   description = description)
		if logo:
			company.logo = logo
			company.save()
			img = Image.open(settings.MEDIA_ROOT + "/{0}".format(company.logo))
			img.thumbnail((200, 200), Image.ANTIALIAS)
			img.save(settings.MEDIA_ROOT + "/{0}".format(company.logo))
		company.categories.clear()					   
		for category in categories:
			company.categories.add(category)
		return HttpResponseRedirect("/catalog/changefirm/{0}/{1}/".format(user.id, change_company))
	return render_to_response("base_change_firm.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))	

def check_website (request):
	if "website" in request.GET and request.GET["website"]:
		error = ""
		website = request.GET.get("website", "")
		if "https" in website:
			domain = website[8:].strip( '/' )
			error = True
		elif "http" in website:
			domain = website[7:].strip( '/' )
		else:
			domain = website.strip( '/' )
			website = "http://" + website 
		url =  urllib2.urlopen("http://bar-navig.yandex.ru/u?ver=2&show=32&url=%s" % website)
		xmldoc = minidom.parse(url)
		xml = xmldoc.getElementsByTagName("tcy")[0]
		tic = xml.getAttribute('value')
		try:
			ip_website = socket.gethostbyname_ex(domain)[2][0]
		except socket.gaierror:
			pass
		if not error:
			try:
				parser = html.HTMLParser(encoding="utf-8")
				try:
					document = html.parse(urllib2.urlopen(website), parser)
					try:
						title = document.xpath('/html/head/title/text()')[0]
					except IndexError:
						pass
					h1_list = []
					for item in document.xpath("//h1/text()"):
						h1_list.append(item)
					h2_list = []
					for item in document.xpath("//h2/text()"):
						h2_list.append(item)
					h3_list = []
					for item in document.xpath("//h3/text()"):
						h3_list.append(item)
				except UnicodeDecodeError:
					pass
			except IOError:
				pass
	return render_to_response("base_check_website.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
