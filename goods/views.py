from django.shortcuts import render
from goods.models import Category, Products


def categories(request):
    categories = Category.objects.all()
    context = {
        "title": "Каталог",
        "categories": categories,
    }
    return render(request, "goods/catalog.html", context)


def products(request):
    products = Products.objects.all()
    context = {
        "title": "Продукт",
        'products': products,
    }
    return render(request, "goods/product.html", context)
