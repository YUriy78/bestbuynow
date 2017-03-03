# --*-- coding: utf-8 --*--
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from bestbuynow.views import custom_proc
from django.core.mail import send_mail
from django.db import IntegrityError
from models import *
from board.models import *
from board.views import gen_pass_auto
from forms import *
import hashlib

@csrf_exempt
def bid(request):
	bid_form = BidForm(request.POST)
	status_list = StatusUser.objects.order_by('-name')
	if request.method == "POST" and bid_form.is_valid():
		city = request.POST.get('city', '')
		city = City.objects.get(id = city)
		status = request.POST.get('status', '')
		status = StatusUser.objects.get(id = status)
		name = request.POST.get('name', '')
		position = request.POST.get('position', '')
		salary = request.POST.get('salary', '')
		experience = request.POST.get('experience', '')
		email = request.POST.get('email', '')
		ip_user = request.META["REMOTE_ADDR"]
		gen_password = gen_pass_auto()
		ip_user = request.META["REMOTE_ADDR"]
		try:
			password = hashlib.md5(gen_password).hexdigest()
		except  UnicodeEncodeError:
			pass
		BidUser.objects.create(city = city, status = status, name = name, position = position, salary = salary, experience = experience, email = email, ip_user = ip_user )
		try:
			user = User(city = city, name = name, login = email, email = email, password = password, ip_user = ip_user)
			user.save()
			send_mail(
				"best-buy-now.ru",
				"Спасибо за регистрацию на сайте http://best-buy-now.ru! \n\r Ваш логин: {0} \n\r ваш пароль: {1}".format(email, gen_password),
				"yuriy@best-buy-now.ru",
				[email],
			)
			request.session['id_session'] = user.id
		except IntegrityError:
			pass
		return HttpResponseRedirect("/burse/bid/")
	return render_to_response("base_bid.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
