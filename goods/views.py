from django.shortcuts import render
from goods.models import Products


def categories(request):
    products = Products.objects.all()
    context = {
        "title": "Каталог",
        'products': products,
    }
    return render(request, "goods/catalog.html", context)


def products(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "title": "Продукт",
        "product": product,
    }
    return render(request, "goods/product.html", context)
