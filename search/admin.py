"""this file represent admin site models"""
from django.contrib import admin
from models.product import Product
from models.substitute import Substitute
from models.category import Categories


admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Substitute)

