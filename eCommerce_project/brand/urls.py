from django.urls import path
from . import views

app_name = "brand"

urlpatterns = [
    path("add/", views.add_brand, name="add_brand"),
    path("all/", views.get_brands, name="all_brands"),
    path("update/<brand_id>", views.update_brand, name="update_brand"),
    path("delete/<brand_id>", views.delete_brand, name="delete_brand"),
]