from django.urls import path
from .views import Brands, Brand, Products, Product

urlpatterns = [
    path("brands/", Brands.as_view(), name="brands"),
    path("brands/<int:pk>/", Brand.as_view(), name="brand"),
    path("products/", Products.as_view(), name="products"),
    path("products/<int:pk>/", Product.as_view(), name="product"),
]
