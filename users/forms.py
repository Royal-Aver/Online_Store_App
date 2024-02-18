from django.contrib.auth.forms import AuthenticationForm
from django import forms
from users.models import User

class UserLoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, "class": 'form-control', "placeholder": 'Введите ваше имя пользователя'}), label='Имя пользователя')
  password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control', "placeholder": 'Введите ваш пароль'}), label='Пароль')
  class Meta:
    model = User
    fields = ('username', 'password')