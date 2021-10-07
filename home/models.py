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
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_of_featured', blank=True, unique=True)
    
    def __str__(self):
        return self.product.name

class Gallery(Featured):
    pass

class UserProfile(models.Model):  
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    contact = models.IntegerField(default=0)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username