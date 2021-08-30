from django.db import models

# Create your models here.

shirt_sizes = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
]

shirt_types = [
    ('HALF', 'HALF'),
    ('FULL', 'FULL'),
]

class Shirt(models.Model):
    shirt_name = models.CharField(max_length=1000, unique=True)
    shirt_size = models.CharField(max_length = 4, choices=shirt_sizes, default='M')
    shirt_type = models.CharField(max_length=4, choices=shirt_types, default='HALF', blank=False)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    price = models.FloatField(default=0, blank=False)

    def __str__(self):
        return self.shirt_name

