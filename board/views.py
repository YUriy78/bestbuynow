# --*-- coding: utf-8 --*--
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from bestbuynow.views import custom_proc
from django.core.mail import send_mail
from django.db.models import Q
from bestbuynow import settings
from models import *
from forms import *
from PIL import Image
import hashlib
import random

def gen_pass(request):
	arr = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 		   
	'd', 'f', 'g', 'h', 'j', 'k', "l", 'z', 'x', 'c', 'v', 'b', 'n', 'm', 
	'1', '2' , '3', '4' , '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 
	'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 
	'Z', 'X', 'C', 'V', 'B', 'N', 'M' 
	]
	passw = []
	for i in range(12):
		passw.append(random.choice(arr))
	return HttpResponse("".join(passw))

def check_login(request):
	status = ""
	try:
		user = User.objects.get(login = request.GET['login'])
	except User.DoesNotExist:
		status = "Свободен"
	else:
		status = "Занят"
	return HttpResponse(status)

@csrf_exempt
def registration(request):
	errors = []
	registration = Registration(request.POST)
	if request.method == "POST" and registration.is_valid():
		city = request.POST.get('city', '')
		name = request.POST.get('name', '')
		login = request.POST.get('login', '')
		email = request.POST.get('email', '')
		password1 = request.POST.get('password1', '')
		password2 = request.POST.get('password2', '')
		city = City.objects.get(id = city)
		ip_user = request.META["REMOTE_ADDR"]
		if name and login and email:
			if password1 == password2:
				if len(password1) >= 8:
					try:
						password1 = hashlib.md5(password1).hexdigest()
					except  UnicodeEncodeError:
						pass
					try:
						user = User(city = city, name = name, login = login, email = email, password = password1, ip_user = ip_user)
						user.save()
						send_mail(
						"best-buy-now.ru",
						"Спасибо за регистрацию на сайте http://best-buy-now.ru!",
						"yuriy@best-buy-now.ru",
						[user.email],
						)
						request.session['id_session'] = user.id
						return HttpResponseRedirect("/board/account/{0}".format(user.id))
					except IntegrityError:
						errors.append("Пользователь с таким логином или email уже существует!")
				else:
					errors.append("Длина пароля должна быть не меньше 8 символов!")
			else:
				errors.append("Ваши пароли не совпадают!")
		else:
			errors.append("Заполните все поля!")
	return render_to_response("base_registration.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))

@csrf_exempt
def user_account(request, id_user):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	change_avatar = ChangeAvatar(request.POST)
	count_messages = Message.objects.filter(user = user).count()
	if request.method == "POST" and change_avatar.is_valid():
		avatar = request.FILES.get("avatar", "")
		user.avatar = avatar
		user.save()
		if user.avatar:
			img = Image.open(settings.MEDIA_ROOT + "/{0}".format(user.avatar))
			img.thumbnail((100, 100), Image.ANTIALIAS)
			img.save(settings.MEDIA_ROOT + "/{0}".format(user.avatar))
	return render_to_response("base_account.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))

@csrf_exempt
def user_login (request):
	errors = []
	login_user = LoginUser(request.POST)
	if request.method == "POST" and login_user.is_valid():
		login = request.POST.get("login", "").strip()
		password = request.POST.get("password", "").strip()
		try: 
			password = hashlib.md5(password).hexdigest()
		except UnicodeEncodeError:
			pass
		try:
			user = User.objects.get(login = login)
			if user.password == password:
				request.session["id_session"] = user.id
				return HttpResponseRedirect("/board/account/{0}".format(user.id))
			else:
				errors.append("Неправильный пароль!")
		except User.DoesNotExist:
			errors.append("Такого пользователя не существует!")
	return render_to_response("base_login.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
@csrf_exempt		
def feedback (request):
	errors = []
	feedback_form = UserFeedback(request.POST)
	if request.method == "POST" and feedback_form.is_valid():
		name = request.POST['name']
		email = request.POST['email']
		text = request.POST['text']
		if name and email and text:
			Feedback.objects.create(name = name, email = email, text = text)
			return HttpResponseRedirect("/board/feedback/")
		else:
			errors.append("Заполните все поля!")	
	return render_to_response("base_feedback.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
@csrf_exempt
def data_change(request, id_user):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	if request.method == "POST":
		city = request.POST.get("city", '')
		name = request.POST.get("name", '')
		login = request.POST.get("login", '')
		email = request.POST.get("email", '')
		phone = request.POST.get("phone", '')
		metro = request.POST.get("metro", '')
		company = request.POST.get("company", '')
		address = request.POST.get("address", '')
		User.objects.filter(id = id_user).update(city = city, name = name, login = login, email = email, phone = phone, metro = metro, company = company, address = address)
		return HttpResponseRedirect("board/datachange/{0}".format(id_user))
	return render_to_response("base_data_change.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
@csrf_exempt
def change_logo(request, id_user):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	change_logo = ChangeLogo(request.POST)
	if request.method == "POST" and change_logo.is_valid():
		logo = request.FILES.get("logo", "")
		user.logo = logo
		user.save()
		if user.logo:
			img = Image.open(settings.MEDIA_ROOT + "/{0}".format(user.logo))
			img.thumbnail((200, 200), Image.ANTIALIAS)
			img.save(settings.MEDIA_ROOT + "/{0}".format(user.logo))
		return HttpResponseRedirect("/board/account/{0}".format(user.id))
	return render_to_response("base_change_logo.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
@csrf_exempt	
def change_pass(request, id_user):
	errors = []
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	change_pass = ChangePassword(request.POST)
	if request.method == "POST" and change_pass.is_valid():
		oldpassword = hashlib.md5(request.POST.get('oldpassword', '')).hexdigest()
		password1 = request.POST.get('password1', '')
		password2 = request.POST.get('password2', '')
		if user.password == oldpassword:
			if password1 == password2:
				if len(password1) >= 8:
					password1 = hashlib.md5(password1).hexdigest()
					user.password = password1
					user.save()
					return HttpResponseRedirect("/board/account/{0}".format(user.id))
				else:
					errors.append("Пароль должен быть не меньше 8 символов!")
			else:
				errors.append("Ваши пароли не совпадают!")
		else:
			errors.append("Вы ввели неправильный старый пароль!")
	return render_to_response("base_change_pass.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))

def add_br (text):
	new_text = ""
	for str in text.split("\n"):
		new_text += str.strip("\n") + "<br/>\n"
	return new_text
	
def subscription (id, cath):
	ver = Verification.objects.get(sign = 'yes')
	sub_list = Subscription.objects.filter(category = cath, verification = ver)
	if sub_list:
		for user in sub_list:
			send_mail(
				"На сайте best-buy-now.ru размещено новое объявление",
				"Ссылка на объявление: http://best-buy-now.ru/board/pagead/{0}/ \n\r\n\r\n\r Отписаться от рассылки можно кликнув по ссылке: http://best-buy-now.ru/board/verification/{1}/?ver=del".format(id, user.id) ,
				"yuriy@best-buy-now.ru",
				[user.email],
			)
			
def change_img(image):
	img = Image.open(settings.MEDIA_ROOT + "/{0}".format(image.file))
	img.thumbnail((550, 550), Image.ANTIALIAS)
	img.save(settings.MEDIA_ROOT + "/{0}".format(image.file))
	
@csrf_exempt	
def new_ad(request, id_user):
	errors = []
	if request.META['HTTP_REFERER'] == 'http://best-buy-now.ru/board/add/':
		errors.append("Заполните все поля!")
	try:	
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session', False):
		right_to_change = True
	new_ad_form = NewAd(request.POST)
	job_main_category = MainCategory.objects.get(name = "Работа")
	if request.method == "POST" and new_ad_form.is_valid():
		user = request.POST.get("user", "")
		user = User.objects.get(id = user)
		category = request.POST.get("category", "")
		category = Category.objects.get(id = category)
		status = Status.objects.get(name = "На проверке")
		priority = Priority.objects.get(name = "Обычный")
		name = request.POST.get("name", "")
		description = add_br(request.POST.get("description", ""))
		price = request.POST.get("price", "")
		if name and len(description) > 6 and price:
			new_ad = Ad(category = category, user = user, city = user.city, status = status, priority = priority, name = name, description = description, price = price)
			new_ad.save()
			subscription(new_ad.id, new_ad.category)
			if new_ad:
				errors.append("Ваше объявление размещено!")
			if request.FILES.getlist("img"):
				for img in request.FILES.getlist("img"):
					try:
						Photo.objects.create(ad = new_ad, file = img)
					except UnicodeEncodeError:
						pass
				new_photo_list = Photo.objects.filter(ad = new_ad)
				for image in new_photo_list:	
					change_img(image)
		else:
			errors.append("Заполните все поля!")
	return render_to_response("base_new_ad.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
@csrf_exempt	
def new_job(request, id_user):
	errors = []
	if request.META['HTTP_REFERER'] == 'http://best-buy-now.ru/board/add/':
		errors.append("Заполните все поля!")
 	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session', False):
		right_to_change = True
	new_job_form = NewJob(request.POST)
	main_category = MainCategory.objects.get(name = "Работа")
	categories = Category.objects.filter(main_category = main_category)
	if request.method == "POST":
		user = request.POST.get("user", "")
		user = User.objects.get(id = user)
		category = request.POST.get("category", "")
		category = Category.objects.get(id = category)
		status = Status.objects.get(name = "На проверке")
		priority = Priority.objects.get(name = "Обычный")
		name = request.POST.get("name", "")
		description = add_br(request.POST.get("description", ""))
		salary = request.POST.get("salary", "")
		if name and len(description) > 6 and salary:
			new_ad = Ad(category = category, user = user, city = user.city, status = status, priority = priority, name = name, description = description, salary = salary)
			new_ad.save()
			subscription(new_ad.id, new_ad.category)
			if new_ad:
				errors.append("Ваше объявление размещено!")
			if request.FILES.getlist("img"):
				for img in request.FILES.getlist("img"):
					try:	
						new_photo = Photo(ad = new_ad, file = img)
						new_photo.save()
					except UnicodeEncodeError:
						pass
				new_photo_list = Photo.objects.filter(ad = new_ad)
				for image in new_photo_list:	
					change_img(image)
		else:
			errors.append("Заполните все поля!")
	return render_to_response("base_new_job.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))

@csrf_exempt	
def page_ad(request, id_ad):
	feedback_form = UserFeedback(request.POST)
	try:
		ad = Ad.objects.select_related("user").get(id = id_ad)
	except Ad.DoesNotExist:
		raise Http404
	img_list = Photo.objects.filter(ad = ad)
	img_first = Photo.objects.filter(ad = ad).first()
	if request.method == "POST" and request.is_ajax():
		user_id = request.POST.get("user_id", "")
		name = request.POST.get("name", "")
		email = request.POST.get("email", "")
		text = request.POST.get("text", "")
		user = User.objects.get(id = user_id)
		Message.objects.create(user = user, name = name, email = email, text = text)
		send_mail(
			"Сообщение от пользователя сайта best-buy-now.ru",
			text,
			email,
			[user.email],
			)
	return render_to_response("base_page_ad.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
@csrf_exempt
def forgot_password(request):
	errors = []
	forgot_pass = ForgotPassword(request.POST)
	if request.method == "POST" and forgot_pass.is_valid():
		email = request.POST.get('email', '')
		if email:
			try:
				user = User.objects.get(email = email)
				send_mail(
				"Best buy now",
				"Для восстановления пароля пройдите по ссылке: http://best-buy-now.ru/board/passemail/{0}".format(user.id),
				"yuriy@best-buy-now.ru",
				[user.email],
				)
				errors.append("Письмо с инструкциями выслано на ваш email")
			except User.DoesNotExist:
				errors.append("Такого email в нашей базе данных нет!")
		else:
			errors.append("Введите ваш email!")
	return render_to_response("base_forgot_pass.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
@csrf_exempt
def password_email(request, id_user):
	errors = []
	pass_email = PasswordEmail(request.POST)
	if request.method == "POST" and pass_email.is_valid():
		user = User.objects.get(id = id_user)
		password1 = request.POST.get('password1', '')
		password2 = request.POST.get('password2', '')
		if password1 == password2:
			if len(password1) >= 8:
				try:
					password1 = hashlib.md5(password1).hexdigest()
				except  UnicodeEncodeError:
					pass
				user.password = password1
				user.save()
				return HttpResponseRedirect("board/passemail/{0}".format(user.id))
			else:
				errors.append("Пароль должен быть не меньше 8 символов!")
		else:
			errors.append("Ваши пароли не совпадают!")
	return render_to_response("base_pass_email.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))

def search(request):
	if "search" in request.GET:
		category = Category.objects.get(id = request.GET['category'])
		city = City.objects.get(id = request.GET['city'])
		status = Status.objects.get(name = "Одобрено")
		if request.GET['search'] == "":
			search = category
			ads = Ad.objects.prefetch_related('photo_set').select_related('category').filter(Q(category = category) & Q(city = city) & Q(status = status)).order_by("-id")
		elif request.GET['search']:
			search = request.GET.get('search', '')
			ads = Ad.objects.prefetch_related('photo_set').select_related('category').filter(Q(name__icontains = search) & Q(category = category) & Q(city = city) & Q(status = status)).order_by("-id")
		paginator = Paginator(ads, 15)
		page = request.GET.get('page', '')
		try:
			ad_list = paginator.page(page)
		except PageNotAnInteger:
			ad_list = paginator.page(1)
		except EmptyPage:
			ad_list = paginator.page(paginator.num_pages)
	else:
		return HttpResponseRedirect("/")
	return render_to_response("base_search.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
def all_user_ad (request, id_user):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	ad_list_user = Ad.objects.prefetch_related('photo_set').filter(user = user)
	paginator = Paginator(ad_list_user, 15)
	page = request.GET.get('page')
	try:
		ad_list = paginator.page(page)
	except PageNotAnInteger:
		ad_list = paginator.page(1)
	except EmptyPage:
		ad_list = paginator.page(paginator.num_pages)
	if "delad" in request.GET and request.GET['delad']:
		ad = Ad.objects.get(id = request.GET['delad'])
		photos = Photo.objects.filter(ad = ad)
		photos.delete()
		ad.delete()
		return HttpResponseRedirect("/board/userad/{0}".format(user.id))
	return render_to_response("base_user_ad.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))

@csrf_exempt
def change_ad (request, id_user, change_ad):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	ad_user = Ad.objects.select_related('category').get(id = change_ad)
	if str(ad_user.category.main_category) == "Работа":
		job_true = True
	if request.method == "POST":
		status = Status.objects.get(name = "На проверке")
		category = request.POST.get("category", "")
		city = request.POST.get("city", "")
		name = request.POST.get("name", "")
		description = request.POST.get("description", "")
		salary = request.POST.get("salary", "")
		price = request.POST.get("price", "")
		if name and description:
			if price:
				Ad.objects.filter(id = ad_user.id).update(name = name, category = category, city = city, description = description, status = status, price = price)
			elif salary:
				Ad.objects.filter(id = ad_user.id).update(name = name, category = category, city = city, description = description, status = status, salary = salary)
			if request.FILES.getlist("img"):
				for img in request.FILES.getlist("img"):
					try:
						new_photo = Photo(ad = ad_user , file = img)
						new_photo.save()
					except UnicodeEncodeError:
						pass
				new_photo_list = Photo.objects.filter(ad = ad_user)
				for image in new_photo_list:	
					change_img(image)
			return HttpResponseRedirect("/board/changead/%s/%s/" % (user.id, ad_user.id))
	return render_to_response("base_change_ad.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
def description_site (request):
	description = Description.objects.get(title = "О сайте")
	return render_to_response("base_description.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
def internal_mail(request, id_user):
	try:
		user = User.objects.get(id = id_user)
	except User.DoesNotExist:
		raise Http404
	if int(user.id) == request.session.get('id_session'):
		right_to_change = True
	messages = Message.objects.filter(user = user)
	if "delmess" in request.GET and request.GET['delmess']:
		del_message = Message.objects.get(id = request.GET.get('delmess', ''))
		del_message.delete()
	return render_to_response("base_user_mail.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
def articles(request):
	articles_list = Article.objects.order_by("-id")
	paginator = Paginator(articles_list, 10)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return render_to_response("base_articles.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))

def article(request, id):
	try: 
		article = Article.objects.get(id = id)
	except Article.DoesNotExist:
		raise Http404
	return render_to_response("base_article.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	

def search_article(request):
	if 'search' in request.GET and request.GET['search']:
		search = request.GET.get("search", "")
		articles = Article.objects.filter(title__icontains = search) | Article.objects.filter(description__icontains = search)
		paginator = Paginator(articles, 10)
		page = request.GET.get('page')
		try:
			articles = paginator.page(page)
		except PageNotAnInteger:
			articles  = paginator.page(1)
		except EmptyPage:
			articles  = paginator.page(paginator.num_pages)
	else:
		return HttpResponseRedirect("/board/articles")
	return render_to_response("base_search_art.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	

def check_verification(request, id):
	if 'ver' in request.GET and request.GET['ver'] == 'yes':
		ver = Verification.objects.get(sign = 'yes')
		try: 
			Subscription.objects.filter(id = id).update(verification = ver)
		except Subscription.DoesNotExist:
			pass
		check_sub = True
		return render_to_response("base_verification.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	elif 'ver' in request.GET and request.GET['ver'] == 'del':
		try: 
			Subscription.objects.filter(id = id).delete()
		except Subscription.DoesNotExist:
			pass
		del_sub = True
		return render_to_response("base_verification.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	else:
		return HttpResponseRedirect("/")
		
def gen_pass_auto():
	arr = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 		   
	'd', 'f', 'g', 'h', 'j', 'k', "l", 'z', 'x', 'c', 'v', 'b', 'n', 'm', 
	'1', '2' , '3', '4' , '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 
	'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 
	'Z', 'X', 'C', 'V', 'B', 'N', 'M' 
	]
	passw = []
	for i in range(12):
		passw.append(random.choice(arr))
	return "".join(passw)

@csrf_exempt	
def add_without_reg (request):
	errors = []
	error = ""
	if request.method == "POST":
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		city = City.objects.get(id = request.POST.get('city', ''))
		gen_password = gen_pass_auto()
		status = Status.objects.get(name = "На проверке")
		category = request.POST.get("category", "")
		category = Category.objects.get(id = category)
		name_ad = request.POST.get("name_ad", "")
		description = add_br(request.POST.get("description", ""))
		salary = request.POST.get("salary", "")
		price = request.POST.get("price", "")
		priority = Priority.objects.get(name = "Обычный")
		try:
			password = hashlib.md5(gen_password).hexdigest()
		except  UnicodeEncodeError:
			pass
		ip_user = request.META["REMOTE_ADDR"]
		if name and email:
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
				errors.append("Пользователь с таким логином или email уже существует!")
				error = True
		else:
			errors.append("Вы не ввели ваше имя и email!")
			error = True
		if not error:
			if name_ad and len(description) > 6 :
				if price or salary:
					if price:
						ad_user = Ad(category = category, user = user, city = user.city, status = status, priority = priority, name = name_ad, description = description, price = price)
						ad_user.save()
					elif salary:
						ad_user = Ad(category = category, user = user, city = user.city, status = status, priority = priority, name = name_ad, description = description, salary = salary)
						ad_user.save()
					if request.FILES.getlist("img"):
						for img in request.FILES.getlist("img"):
							try:	
								new_photo = Photo(ad = ad_user, file = img)
								new_photo.save()
							except UnicodeEncodeError:
								pass
					new_photo_list = Photo.objects.filter(ad = ad_user)
					for image in new_photo_list:	
						change_img(image)
					return HttpResponseRedirect("/board/userad/{0}".format(user.id))
				else:
					return HttpResponseRedirect("/board/account/{0}".format(user.id))
			else:
				if price:
					return HttpResponseRedirect("/board/newad/{0}".format(user.id))
				elif salary:
					return HttpResponseRedirect("/board/newjob/{0}".format(user.id))
				else:
					return HttpResponseRedirect("/board/account/{0}".format(user.id))
	return render_to_response("base_add.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
	
def interactive(request, id):
	category = Category.objects.get(id = id)
	search = category
	status = Status.objects.get(name = "Одобрено")
	ads = Ad.objects.filter(category = category, status = status).order_by("-id")
	paginator = Paginator(ads, 15)
	page = request.GET.get('page', '')
	try:
		ad_list = paginator.page(page)
	except PageNotAnInteger:
		ad_list = paginator.page(1)
	except EmptyPage:
		ad_list = paginator.page(paginator.num_pages)
	return render_to_response("base_search.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))
