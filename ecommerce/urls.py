from django.urls import path
from .views import add_brand, add_product, list_brand, list_product, update_brand, update_product, delete_brand, deleted_product
app_name = 'ecommerce'

urlpatterns = [
    # post
    path('brand/add/', add_brand, name='add_brand'),
    path('product/add/', add_product, name='add_product'),
    # get
    path('brand/', list_brand, name='list_brand'),
    path('product/', list_product, name='list_product'),
    # put
    path('brand/update/<id>/', update_brand, name='update_brand'),
    path('product/update/<id>/', update_product, name='update_product'),
    # delete
    path('brand/delete/<id>/', delete_brand, name='delete_brand'),
    path('product/delete/<id>/', deleted_product, name='delete_product'),
]

