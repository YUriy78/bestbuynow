# --*-- coding: utf-8 --*--
from django.db import models
from bestbuynow import settings
from PIL import Image

class MainCategory (models.Model):
	name = models.CharField(max_length=100, verbose_name="Главная категория", unique = True)
		
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Главная категория"
		verbose_name_plural = u"Главные категории"
		
class Category(models.Model):
	main_category = models.ForeignKey(MainCategory)
	name = models.CharField(max_length=100, verbose_name="Категория", unique = True )
	
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Категория"
		verbose_name_plural = u"Категории"
		
class City (models.Model):
	name = models.CharField(max_length=100, verbose_name="Город", unique = True)
	
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Город"
		verbose_name_plural = u"Города"
		
class User(models.Model):
	city = models.ForeignKey(City)
	login = models.CharField(max_length=100, verbose_name = "Логин пользователя", unique = True)
	company = models.CharField(max_length=200, verbose_name = "Название компании", blank=True)
	address = models.TextField(verbose_name = "Адрес компании", blank=True)
	logo = models.FileField(upload_to='logo', verbose_name = "Логотип компании", blank=True)
	name = models.CharField(max_length=200, verbose_name = "Имя пользователя")
	phone = models.CharField(max_length = 100, verbose_name = "Телефон пользователя", blank=True)
	email = models.EmailField(verbose_name = "Email пользователя", unique = True)
	metro = models.CharField(max_length=100, verbose_name = "Ближайшее метро", blank=True)
	password = models.CharField(max_length = 100, verbose_name = "Пароль")
	avatar = models.FileField(upload_to='avatar', verbose_name = "Аватарка", blank=True)
	ip_user = models.IPAddressField(verbose_name="IP адрес пользователя", blank=True)
		
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Пользователь"
		verbose_name_plural = u"Пользователи"		
	
class Feedback(models.Model):
	name = models.CharField(max_length=200, verbose_name="Имя пользователя")
	email = models.EmailField(verbose_name="Email пользователя")
	text = models.TextField(verbose_name="Текст сообщения")
	date = models.DateField(auto_now_add=True, verbose_name="Дата сообщения")
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name=u"Сообщение администратору"
		verbose_name_plural=u"Сообщения администратору"
		
class Status (models.Model):
	name = models.CharField(max_length=100, verbose_name="Статус объявления")
	
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Статус объявлений"
		verbose_name_plural = u"Статусы объявлений"
		
class Priority (models.Model):
	name = models.CharField(max_length=100, verbose_name="Приоритет объявления")
	
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Приоритет объявлений"
		verbose_name_plural = u"Приоритеты объявлений"
		
		
class Ad (models.Model):
	category = models.ForeignKey(Category)
	user = models.ForeignKey(User)
	city = models.ForeignKey(City)
	status = models.ForeignKey(Status)
	priority = models.ForeignKey(Priority)
	name = models.CharField(max_length=200, verbose_name = "Название объявления", blank=True)
	description = models.TextField(verbose_name = "Описание объвления", blank=True)
	price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True, verbose_name = "Цена")
	salary = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True, verbose_name = "Зарплата")
	date = models.DateField(auto_now_add = True, verbose_name = "Дата публикации объявления")
	
	def __unicode__( self ):
		return u'%s - Статус: %s' % (self.name, self.status)
	
	class Meta:
		verbose_name = u"Объявление"
		verbose_name_plural = u"Объявления"
		
class Message(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=200, verbose_name="Имя отправителя")
	email = models.EmailField(verbose_name="Email отправилеля")
	text = models.TextField(verbose_name="Текст сообщения")
	date = models.DateField(auto_now_add=True, verbose_name="Дата сообщения")
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name=u"Сообщение пользователю"
		verbose_name_plural=u"Сообщения пользователю"
		
class Photo (models.Model):
	ad = models.ForeignKey(Ad)
	file = models.ImageField(upload_to = "ad", verbose_name="Файл картинки")
	
	def __unicode__(self):
		return self.ad.name
		
	class Meta:
		verbose_name=u"Фотография объявления"
		verbose_name_plural=u"Фотографии объявлений"
		
class Description (models.Model):
	title = models.CharField(max_length=200, verbose_name="Заголовок описания")
	text = models.TextField(verbose_name="Текст описания")
	
	def __unicode__(self):
		return self.title
		
	class Meta:
		verbose_name=u"Описание сайта"
		verbose_name_plural=u"Описания сайта"
		
class Article (models.Model):
	title = models.CharField(max_length=300, verbose_name="Название статьи")
	keywords = models.CharField(max_length=200, verbose_name="Ключевые слова")
	thumbnail = models.ImageField(upload_to='articles', verbose_name = "Миниатюра")
	description = models.TextField(verbose_name="Описание статьи")
	text = models.TextField(verbose_name="Текст статьи")
	author = models.CharField(max_length=100, verbose_name="Автор статьи")
	date = models.DateField(auto_now_add=True, verbose_name="Дата статьи")
	
	def save(self, *args, **kwargs):
		super(Article, self).save(*args, **kwargs)
		if self.thumbnail:
			img = Image.open(settings.MEDIA_ROOT + "/{0}".format(self.thumbnail))
			img.thumbnail((100, 100), Image.ANTIALIAS)
			img.save(settings.MEDIA_ROOT + "/{0}".format(self.thumbnail))
	
	def __unicode__( self ):
		return self.title
	
	class Meta:
		verbose_name = u"Статья"
		verbose_name_plural = u"Статьи"

class Verification(models.Model):
	sign = models.CharField(max_length=5, verbose_name="Подтверждение подписки")
	
	def __unicode__(self):
		return self.sign
		
	class Meta:
		verbose_name=u"Подтверждение подписок"
		verbose_name_plural=u"Подтверждения подписок"
		
class Subscription(models.Model):
	email = models.EmailField(verbose_name="Email подписчика")
	category = models.ForeignKey(Category)
	verification = models.ForeignKey(Verification)
	
			
	def __unicode__(self):
		return self.email
		
	class Meta:
		verbose_name=u"Подписка на объявления"
		verbose_name_plural=u"Подписки на объявления"
		
class IconMainCategory(models.Model):
	main_category = models.ForeignKey(MainCategory)
	icon = models.FileField(upload_to='icon', verbose_name = "Иконка", blank=True)

	class Meta:
		verbose_name=u"Иконка"
		verbose_name_plural=u"Иконки"
