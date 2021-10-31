from django.db import models
from product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Item(models.Model):
    name = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product_of_item", null=True, unique=True)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.name