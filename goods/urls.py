from django.urls import path

from goods.views import categories, products

app_name = 'goods'

urlpatterns = [
  path('category/<slug:category_slug>/', categories, name='category'),
  path('category/<slug:category_slug>/<int:page>', categories, name='category'),
  path('product/<slug:product_slug>/', products, name='product'),
  ]