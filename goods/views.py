from django.shortcuts import get_list_or_404, render
from goods.models import Products
from django.core.paginator import Paginator


def categories(request, category_slug, page=1):
    if category_slug == 'vse':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(products, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Каталог",
        'products': current_page,
        'slug_url': category_slug,
    }
    return render(request, "goods/catalog.html", context)


def products(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "title": "Продукт",
        "product": product,
    }
    return render(request, "goods/product.html", context)
