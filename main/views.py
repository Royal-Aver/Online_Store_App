from django.shortcuts import render
from goods.models import Category

def index(request):
  categories = Category.objects.all()
  context = {
    'title': 'Главная',
    "categories": categories,
  }
  return render(request, 'main/index.html', context)

def about(request):
  context = {
    'title': 'О нас',
  }
  return render(request, 'main/about.html', context)
