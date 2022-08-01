from django.urls import path
from . import views

app_name = 'orm'

urlpatterns = [
    path('add/', views.add_brand, name='add_brand'),
    path('list/', views.list_brand, name='list_brand'),
    path('update/<brand_id>/', views.update_brand, name='update_brand'),
    path('delete/<brand_id>/', views.remove_brand , name='remove_brand'),
    path('search/', views.search_brand, name='search_brand'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/list/', views.list_product, name='list_products'),
    path('products/update/<product_id>/', views.update_product, name='update_product'),
    path('products/delete/<product_id>/', views.delete_product, name='delete_product'),
    path('products/specified_list/', views.list_products_of_brand, name='list products of brand')
]