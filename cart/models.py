from django.db import models
from product.models import Product
# Create your models here.
class Item(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_of_item", null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.name