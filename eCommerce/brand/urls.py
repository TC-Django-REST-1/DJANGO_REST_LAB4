from django.urls import path

from . import views

app_name = "brand"

urlpatterns = [
    path("add/", views.add_brand, name="add_brand"),
    path("all/", views.list_brands, name="list_brands"),
    path("update/<brand_id>/", views.update_brand, name="update_brand"),
    path("delete/<brand_id>/", views.delete_brand, name="delete_brand"),
    
    path("products/add/", views.add_product, name="add_product"),
    path("products/all/", views.list_products, name="list_products"),
    path("products/update/<product_id>/", views.update_product, name="update_product"),
    path("products/delete/<product_id>/", views.delete_product, name="delete_product"),
    path("products/get/<product_id>/", views.get_product, name="get_product"),

]
