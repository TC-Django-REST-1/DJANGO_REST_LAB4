from django.urls import path
from . import views

urlpatterns = [
    path('brand/all/', views.list_brands),
    path('brand/add/', views.add_brand),
    path('brand/update/<brand_id>', views.update_brand),
    path('brand/delete/<brand_id>', views.delete_brand),
    # product
    path('product/all/<product_id>', views.list_product),
    path('product/add/', views.add_product),
    path('product/update/<product_id>', views.update_product),
    path('product/delete/<product_id>', views.delete_product),
    path('product/brand/<brand_id>', views.list_products_of_brand),
]