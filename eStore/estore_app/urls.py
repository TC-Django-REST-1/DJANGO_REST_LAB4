from django.urls import path
from . import views

app_name = "estore_app"

urlpatterns = [
    #Brand
    path("add/brand", views.new_brand, name="new_brand"),
    path("all/brands", views.read_brand, name="read_brand"),
    path("update/brand/<brand_id>", views.update_brand, name="update_brand"),
    path("delete/brand/<brand_id>", views.delete_brand, name="delete_brand"),
    #Product
    path("add/product", views.new_product, name="new_product"),
    path("all/products", views.read_product, name="read_product"),
    path("update/product/<product_id>", views.update_product, name="update_product"),
    path("delete/product/<product_id>", views.delete_product, name="delete_product"),
    #Spicific
    path("products/brand/<brand_id>",views.products_of_brand,name="products_of_brand"),
    path("limited/brands/",views.limited_list_brand,name="limited_list_brand"),
    path("limited/products/",views.limited_list_product,name="limited_list_product"),

    #Search
    path("search/<brand_title>",views.search,name="search"),

]