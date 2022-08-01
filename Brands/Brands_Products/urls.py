from django.urls import path
from . import views
app_name = "Brands"


urlpatterns = [
    # Brands urls
    path('Brand/Create', views.create_brand, name='create_brand'),
    path('Brand/list', views.list_brand, name='list_brand'),
    path('Brand/update/<brand_id>/', views.update_brand, name='update_brand'),
    path('Brand/delete/<brand_id>/', views.delete_brand, name='delete_brand'),
    path('Brand/search/<str:brand_name>/', views.get_brandName, name='get_brandName'),

    # Product urls
    path('Product/Create', views.create_product, name='create_product'),
    path('Product/list', views.list_product, name='list_product'),
    path('Product/update/<product_id>/', views.update_product, name='update_product'),
    path('Product/delete/<product_id>/', views.delete_product, name='delete_product'),
]