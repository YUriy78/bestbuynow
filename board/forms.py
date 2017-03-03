# --*-- coding: utf-8 --*--
from django import forms
	
class Registration (forms.Form):
	name = forms.CharField(label="Ваше имя", required=False)
	login = forms.CharField(label="Логин", required=False)
	email = forms.EmailField(label="Email", required=False)
	password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=False)
	password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput, required=False)
	
class LoginUser(forms.Form):
	login = forms.CharField(label="Логин", required=False)
	password = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=False)
	
class UserFeedback(forms.Form):
	name = forms.CharField(label="Ваше имя", required=False)
	email = forms.EmailField(label="Ваше email", required=False)
	text = forms.CharField(label="Текст сообщения", widget=forms.Textarea, required=False)
	
class ChangeLogo(forms.Form):
	logo = forms.FileField(label="Логотип добавить/изменить:", required=False)
	
class ChangeAvatar(forms.Form):
	avatar = forms.FileField(label="Аватарка", required=False)
	
class ChangePassword(forms.Form):
	oldpassword = forms.CharField(label="Ващ старый пароль", widget=forms.PasswordInput, required=False)
	password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput, required=False)
	password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput, required=False)
	
class NewAd (forms.Form):
	name = forms.CharField(label="Заголовок", required=False)
	description = forms.CharField(label="Текст объявления (перевод строки: <br/>)", widget=forms.Textarea, required=False)
	price =  forms.DecimalField(label="Цена", required=False)
	
class NewJob (forms.Form):
	name = forms.CharField(label="Должность", required=False)
	description = forms.CharField(label="Текст вакансии/резюме (перевод строки: <br/>)", widget=forms.Textarea, required=False)
	salary =  forms.DecimalField(label="Зарплата", required=False)
	
class ForgotPassword(forms.Form):
	email = forms.EmailField(label="Email, использованный при регистрации", required=False)
	
class PasswordEmail(forms.Form):
	password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput, required=False)
	password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput, required=False)



	