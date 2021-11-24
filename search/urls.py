from django.urls import path
from . import views

app_name = "search"
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("legal_notice/", views.legal_notice, name="legal_notice")
]
