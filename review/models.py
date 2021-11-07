from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from product.models import Product
# Create your models here.

class ReviewImage(models.Model):
    image = models.ImageField(upload_to='user_review_images/%Y/%m/%d/', blank = True, default = "None", null=True)

    def __str__(self):
        return str(self.image)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_of_review')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_of_review')
    rating = models.PositiveSmallIntegerField(blank=True, default = 0, validators = [MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(ReviewImage, related_name='image_of_review', blank=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username