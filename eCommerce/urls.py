from django.urls import path
from . import views

brand = "Brand"
product = "Product"

urlpatterns = [
    # brand

    path(f'{brand}/create', views.add_brand),
    path(f'{brand}/read', views.list_brand),
    path(f'{brand}/update/<str:brand_title>', views.update_brand),
    path(f'{brand}/delete/<str:brand_title>', views.delete_brand),

    # prodect

    path(f'{product}/create', views.add_Product),
    path(f'{product}/read', views.list_Products),
    path(f'{product}/update/<str:product_id>', views.update_product),
    path(f'{product}/delete/<str:product_id>', views.delete_product),
]
