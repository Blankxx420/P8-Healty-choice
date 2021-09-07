from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name