from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_brand, name="add_brand"),
    path("all/", views.list_brands, name="list_brands"),
    path("update/<brand_id>/", views.update_brand, name="update_brand"),
    path("delete/<brand_id>/", views.delete_brand, name="delete_brand"),

    path("product/add/", views.add_product, name="add_product"),
    path("product/all/", views.list_products, name="list_products"),
    path("product/update/<product_id>/", views.update_product, name="update_product"),
    path("product/delete/<product_id>/", views.delete_product, name="delete_product"),

]