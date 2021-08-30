from django.db import models

# Create your models here.

tshirt_sizes = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL')
]

tshirt_types = [
    ('HALF', 'HALF'),
    ('FULL', 'FULL'),
]

class Tshirt(models.Model):
    tshirt_name = models.CharField(max_length=1000, unique=True)
    tshirt_size = models.CharField(max_length = 4, choices=tshirt_sizes, default='M')
    tshirt_type = models.CharField(max_length=4, choices=tshirt_types, default='HALF', blank=False)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    price = models.FloatField(default=0, blank=False)

    def __str__(self):
        return self.tshirt_name

