from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    # Brans urls
    path('create_brand/', views.create_brand, name='create_brand'),
    path('list_brands/', views.list_brands, name='list_brands'),
    path('update_brand/<int:brand_id>/', views.update_brand, name='update_brand'),
    path('delete_brand/<int:brand_id>/', views.delete_brand, name='delete_brand'),
    path('get_brand/<str:brand_name>/', views.get_brand_by_name, name='get_brand_by_name'),

    # Products urls
    path('create_product/', views.create_product, name='create_brand'),
    path('list_products/', views.list_products, name='list_brands'),
    path('update_product/<int:product_id>/', views.update_product, name='update_brand'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_brand'),
    path('brand_products/<str:brand_name>/', views.list_products_of_brand, name='brand_products')
]