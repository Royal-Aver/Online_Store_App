from django.shortcuts import render
from goods.models import Products


def categories(request):
    products = Products.objects.all()
    context = {
        "title": "Каталог",
        'products': products,
    }
    return render(request, "goods/catalog.html", context)


def products(request):

    context = {
        "title": "Продукт",

    }
    return render(request, "goods/product.html", context)
