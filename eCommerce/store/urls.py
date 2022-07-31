from django.urls import path
from . import views

app_name = "store"

urlpatterns = {
    # Brand
    path('brand/list/', views.list_brand),
    path('brand/add/', views.add_brand),
    path('brand/update/<brand_id>/', views.brand_update),
    path('brand/delete/<brand_id>/', views.brand_del),

    # Product
    path('product/list/', views.list_product),
    path('product/add/', views.add_product),
    path('product/update/<product_id>/', views.product_update),
    path('product/delete/<product_id>/', views.product_del),
}