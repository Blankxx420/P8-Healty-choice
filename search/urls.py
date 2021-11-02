from django.urls import path
from . import vien

app_name = "search"
urlpatterns = [
    path('', home),
    path("products/", products, name=products)
]
