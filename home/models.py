from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import *
# Create your models here.
class User(AbstractUser):
    pass

class CarouselImage(models.Model):
    i1 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True)
    i2 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True)
    i3 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True)

class Featured(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_of_featured', blank=True)
    
    def __str__(self):
        return self.product.name