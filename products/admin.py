from django.contrib import admin
from .models import Brands, Products


admin.register(Brands, Products)
