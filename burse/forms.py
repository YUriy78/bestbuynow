# --*-- coding: utf-8 --*--
from django import forms
from models import *
	
class BidForm(forms.Form):
	name = forms.CharField(label="Полное имя:")
	position = forms.CharField(label="Должность:")
	salary = forms.DecimalField(label="Зарплата:", required=False)
	experience = forms.IntegerField(label="Опыт:", required=False)
	email = forms.EmailField(label="Email")
	
	
	




	