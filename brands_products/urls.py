from django.urls import path

from . import views

app_name = "brands_products"

urlpatterns = [
    path("brands/create/", views.add_brand, name="add_brand"),
    path("brands/read/", views.list_brands, name="list_brands"),
    path("brands/update/<brand_id>/", views.update_brand, name="update_brand"),
    path("brands/delete/<brand_id>/", views.delete_brand, name="delete_brand"),

    path("create/", views.add_product, name="add_product"),
    path('brand_products/<brand_id>/', views.list_brand_products, name="list_brand_products"),
    path("read/", views.list_products, name="list_products"),
    path("update/<product_id>/", views.update_product, name="update_product"),
    path("delete/<product_id>/", views.delete_product, name="delete_product"),
]