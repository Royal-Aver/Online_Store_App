from django.shortcuts import render


def login(request):
    context = {
        "title": "Логин",
    }

    return render(request, "users/login.html")


def profile(request):
    context = {
        "title": "Профиль",
    }

    return render(request, "users/profile.html")


def registration(request):
    context = {
        "title": "Регистрация пользователя",
    }

    return render(request, "users/registration.html")