from django.urls import path, include
from . import urls2

urlpatterns = [
    path('Brand/', include(urls2)),
    path('Product/', include(urls2)),
]
