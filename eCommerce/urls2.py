from django.urls import path
from . import views

urlpatterns = [
    path('create', views.add_brand),
    path('read', views.list_brand),
    path('update/<str:brand_title>', views.update_brand),
    path('delete/<str:brand_title>', views.delete_brand),
]
