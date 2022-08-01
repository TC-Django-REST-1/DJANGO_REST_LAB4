from django.urls import path
from .views import add_brand, add_product, list_brand, list_product
app_name = 'ecommerce'

urlpatterns = [
    # post
    path('brand/add/', add_brand, name='add_brand'),
    path('product/add/', add_product, name='add_product'),
    # get
    path('brand/', list_brand, name='list_brand'),
    path('product/', list_product, name='list_product'),
]

