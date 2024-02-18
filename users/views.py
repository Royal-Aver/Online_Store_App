from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        "title": "Логин",
        'form': form,
    }

    return render(request, "users/login.html", context)


def profile(request):
    context = {
        "title": "Профиль",
    }

    return render(request, "users/profile.html", context)


def registration(request):
    context = {
        "title": "Регистрация пользователя",
    }

    return render(request, "users/registration.html", context)