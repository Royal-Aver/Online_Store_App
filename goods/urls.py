from django.urls import path

from goods.views import catalog, product

app_name = 'goods'

urlpatterns = [
  path('catalog/', catalog, name='catalog'),
  path('product', product, name='product'),
  ]