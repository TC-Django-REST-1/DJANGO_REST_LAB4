from django.urls import path

from . import views

app_name = "brands_products"

urlpatterns = [
    path("brands/create/", views.create_brand, name="create_brand"),
    path("brands/read/", views.read_brands, name="read_brands"),
    path("brands/update/<brand_id>/", views.update_brand, name="update_brand"),
    path("brands/delete/<brand_id>/", views.delete_brand, name="delete_brand"),

    path("create/", views.create_product, name="add_product"),
    path('brand_products/<brand_id>/', views.read_brand_products, name="list_brand_products"),
    path("read/", views.read_products, name="list_products"),
    path("update/<product_id>/", views.update_product, name="update_product"),
    path("delete/<product_id>/", views.delete_product, name="delete_product"),
]