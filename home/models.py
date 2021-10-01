from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class CarouselImage(models.Model):
    i1 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True)
    i2 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True)
    i3 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True)