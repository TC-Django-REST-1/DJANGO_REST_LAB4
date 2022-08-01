from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
   
    path("brand/add", views.add_brand, name="add_brand"),
    path("product/add", views.add_product, name="add_product"),
    
    path("brand/list", views.list_brand, name="list_brand"),
    path("brand/list/<search>", views.list_brand, name="list_brand"),
    path("product/list", views.list_product, name="list_product"),
    
    path("brand/delete/<brand_id>/", views.delete_brand, name="delete_brand"),
    path("product/delete/<product_id>/", views.delete_product, name="delete_product"),

    path("brand/update/<brand_id>/", views.update_brand, name="update_brand"),
    path("product/update/<product_id>/", views.update_product, name="update_product"),

    path("products_of_brand/<brand_id>/",views.brand_all_product,name="brand_all_product"),

]