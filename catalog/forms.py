# --*-- coding: utf-8 --*--
from django import forms
from models import *
	
class CompanyForm(forms.Form):
	category = forms.ModelMultipleChoiceField(label="Категория", queryset=CategoryCompany.objects.all())
	company = forms.CharField(label="Название фирмы")
	address = forms.CharField(label="Адрес фирмы")
	metro = forms.CharField(label="Метро", required=False)
	phone = forms.CharField(label="Телефон")
	fax = forms.CharField(label="Факс", required=False)
	icq = forms.CharField(label="ICQ", required=False)
	website = forms.CharField(label="Официальный сайт фирмы", required=False)
	email = forms.EmailField(label="E-mail", required=False)
	opening_times = forms.CharField(label="Время работы", required=False)
	description = forms.CharField(label="Описание деятельности", widget=forms.Textarea, required=False)
	logo = forms.FileField(label="Логотип", required=False)
	
	
	




	