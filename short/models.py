from django.db import models

# Create your models here.
short_types = [
    ('RUNNING', 'RUNNING'),
    ('CARGO', 'CARGO'),
    ('PLEATED', 'PLEATED'),
    ('FLAT FRONT', 'FLAT FRONT'),
    ('DENIM', 'DENIM'),
    ('SWIMMING TRUNKS', 'SWIMMING TRUNKS'),
    ('BERMUDA', 'BERMUDA'),
]

short_sizes = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
]

class Short(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    short_type = models.CharField(max_length=15, choices=short_types, default='BERMUDA')
    short_size = models.CharField(max_length=4, choices=short_sizes, default='M')
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    price = models.FloatField(default=0, blank=False)

    def __str__(self):
        return self.name

