# --*-- coding: utf-8 --*--
from django.db import models
from board.models import *

class CategoryCompany(models.Model):
	name = models.CharField(max_length=100, verbose_name="Категория фирм")
	
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Категория фирм"
		verbose_name_plural = u"Категории фирм"
		
class UserCompany (models.Model):
	user_account = models.ForeignKey(User)
	city = models.ForeignKey(City)
	categories = models.ManyToManyField(CategoryCompany)
	status = models.ForeignKey(Status)
	company = models.CharField(max_length=300, verbose_name = "Название компании")
	address = models.TextField(verbose_name = "Адрес компании")
	metro = models.CharField(max_length=100, verbose_name = "Метро", blank=True)
	phone = models.CharField(max_length = 100, verbose_name = "Телефон компании")
	fax = models.CharField(max_length = 100, verbose_name = "Факс компании", blank=True)
	icq = models.CharField(max_length = 100, verbose_name = "ICQ компании", blank=True)
	website = models.URLField(verbose_name = "Сайт компании", blank=True)
	email = models.EmailField(verbose_name = "Email компании", blank=True)
	opening_times = models.CharField(max_length = 100, verbose_name = "Время работы", blank=True)
	description = models.TextField(verbose_name = "Описание деятельности", blank=True)
	logo = models.ImageField(upload_to='logo', verbose_name = "Логотип компании", blank=True)
	date = models.DateField(auto_now_add=True, verbose_name="Дата размещения в каталоге")
		
	
	def __unicode__( self ):
		return self.company
	
	class Meta:
		verbose_name = u"Фирма"
		verbose_name_plural = u"Фирмы"
