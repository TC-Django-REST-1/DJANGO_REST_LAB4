from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_new_brand/', views.add_brand, name='add_new_brand'),
    path('brands_list/', views.brand_list, name='brand_list'),
    path('update_brand/<brand_id>', views.update_brand, name='update_brand'),
    path('remove_brand/<brand_id>', views.remove_brand, name='remove_brand'),

    path('brand_products/<brand_title>', views.brand_products_list, name='brand_products_list'),
    
    path('add_new_product/', views.add_product, name='add_new_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('update_product/<product_id>', views.update_product, name='update_product'),
    path('remove_product/<product_id>', views.remove_product, name='remove_product'),
]