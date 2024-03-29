from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


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


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        "title": "Профиль",
        "form": form,
    }

    return render(request, "users/profile.html", context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context = {
        "title": "Регистрация пользователя",
        'form': form,
    }

    return render(request, "users/registration.html", context)


def users_cart(request):
    return render(request, "users/users_cart.html")


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))