from django.db import models
from .product import Product


class Substitute(models.Model):
    product_id = models.ForeignKey(Product)
    substitute_id = models.ForeignKey(Product)
