from django.urls import path
from . import views 

app_name = "my_app"

urlpatterns = [
    path("add/", views.add_brand, name="add_brand"),
    path("all/", views.list_brand, name="list_all_brands"),
    path("update/<brand_id>/", views.update_brand, name="update_brand"),
    path("delete/<brand_id>/", views.delete_brand, name="delete_brand"),
    ## products
    path("products/add/", views.add_product, name="add_products"),
    path("products/all/", views.list_product, name="all_products"),
    path("products/update/<product_id>/", views.update_product, name="update_product"),
    path("products/delete/<product_id>/", views.delete_product, name="delete_product"),
    path("products/<str:brand_title>/", views.get_product_of_brand, name="get_prodcts_of_brand")
]