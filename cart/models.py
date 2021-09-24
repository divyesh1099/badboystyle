from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="image")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name="available")
    quantity = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name