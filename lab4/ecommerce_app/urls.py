
import imp
from django.urls import URLPattern, path 
from . import views

app_name = "ecommerce_app"

urlpatterns = [
    path("brand/add/", views.add_brand,name="add_brand"),
    path("brand/all/", views.list_brand,name="list_brand"),
    path("brand/update/<brand_id>/", views.update_brand,name="update_brand"),
    path("brand/delete/<brand_id>", views.delete_brand,name="delete_brand"),

    path("product/add/", views.add_product,name="add_product"),
    path("product/all/", views.list_Product,name="list_Product"),
    path("product/update/<product_id>/", views.update_product,name="update_product"),
    path("product/delete/<product_id>", views.delete_product,name="delete_product")
]