from django.shortcuts import get_list_or_404, render
from goods.models import Products


def categories(request, category_slug):
    if category_slug == 'vse':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
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
