from typing import Tuple
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from product.models import Product
# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_of_review')
    product = models.OneToOneField(Product, related_name="product_of_review", on_delete=models.CASCADE, unique=True)
    rating = models.PositiveSmallIntegerField(blank=True, default = 0, validators = [MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # images = models.ManyToManyField(ReviewImage, related_name='image_of_review', blank=True)
    # images = models.ImageField(blank = True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " | " + self.product.name

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_review_images/%Y/%m/%d/')
    def __str__(self):
        return self.review.product.name + " | " + self.review.user.username