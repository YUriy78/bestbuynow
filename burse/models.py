# --*-- coding: utf-8 --*--
from django.db import models
from board.models import City

class StatusUser (models.Model):
	name = models.CharField(max_length=100, verbose_name="Статус пользователя", unique = True)
		
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Статус пользователя"
		verbose_name_plural = u"Статусы пользователей"
		
		
class BidUser(models.Model):
	status = models.ForeignKey(StatusUser)
	city = models.ForeignKey(City)
	name = models.TextField(verbose_name = "Имя пользователя биржи")
	position = models.TextField(verbose_name = "Должность")
	salary = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True, verbose_name = "Зарплата")
	experience = models.IntegerField(blank=True, null=True, verbose_name = "Стаж работы")
	email = models.EmailField(verbose_name = "Email пользователя биржи")
	ip_user = models.IPAddressField(verbose_name="IP адрес пользователя", blank=True)

		
	def __unicode__( self ):
		return self.name
	
	class Meta:
		verbose_name = u"Заявка пользователя"
		verbose_name_plural = u"Заявки пользователей"		
