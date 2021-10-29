from django.db import models
from product.models import Product
# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=500)
    details = models.TextField(blank=True)
    # discount = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
    product = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.name
    