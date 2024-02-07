from django.urls import path

from goods.views import categories, products

app_name = 'goods'

urlpatterns = [
  path('category/', categories, name='category'),
  path('product/', products, name='product'),
  ]