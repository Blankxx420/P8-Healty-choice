from django.urls import path
from . import views

app_name = "search"
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("products/", views.products, name="products"),
]
