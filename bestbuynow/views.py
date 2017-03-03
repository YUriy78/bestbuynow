# --*-- coding: utf-8 --*--
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.core.mail import send_mail
from board.models import *
import random


def custom_proc(request) :
	main_categories = MainCategory.objects.prefetch_related('category_set').prefetch_related('iconmaincategory_set').order_by("name")
	city_list = City.objects.order_by("name")
	current_user = request.session.get('id_session', '')
	return {
	'main_categories': main_categories,
	'city_list': city_list,
	'current_user': current_user,
	}

@csrf_exempt
def index(request):
	if 'del_session' in request.GET:
		del request.session["id_session"]
		return HttpResponseRedirect("/")
	if request.method == "POST" and request.POST['email']:
		email = request.POST.get('email', '')
		id_category = request.POST.get('category', '')
		category = Category.objects.get(id = id_category)
		verification = Verification.objects.get(sign = "not")
		subscription = Subscription(email = email, category = category, verification = verification)
		subscription.save()
		send_mail(
			"Оформленная подписка на сайте best-buy-now.ru",
			"Подтвердите оформленную подписку кликнув по ссылке http://best-buy-now.ru/board/verification/{0}/?ver=yes".format(subscription.id),
			"yuriy@best-buy-now.ru",
			[email],
			)
		return HttpResponseRedirect("/")
	ten_articles = Article.objects.order_by("-id")[0:10]
	status = Status.objects.get(name = "Одобрено")
	priority = Priority.objects.get(name = "Высокий")
	ad_list = Ad.objects.filter(status = status, priority = priority).prefetch_related('photo_set').select_related('category').order_by("-id")[:20]
	return render_to_response("base_index.html", locals(), context_instance=RequestContext(request, processors=[custom_proc]))