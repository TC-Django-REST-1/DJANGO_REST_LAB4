"""eCommerce_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_eCommerce_app, name="add_eCommerce_app"),
    path("all/", views.list_eCommerce_apps, name="list_eCommerce_app"),
    path("update/<eCommerce_app_id>/", views.update_eCommerce_app, name="update_eCommerce_app"),
    path("delete/<eCommerce_app_id>/", views.delete_eCommerce_app, name="delete_eCommerce_app"),

    path("product/add/", views.add_product, name="add_product"),
    path("product/all/", views.list_products, name="list_products"),
    path("product/update/<product_id>/", views.update_product, name="update_product"),
    path("product/delete/<product_id>/", views.delete_product, name="delete_product"),

]