from django.db import models

# Create your models here.
jean_types = [
    ('LOOSE FIT', 'LOOSE FIT'),
    ('SLIM FIT', 'SLIM FIT'),
]

jean_sizes = [
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
]

class Jean(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    jean_type = models.CharField(max_length=9, choices=jean_types, default='LOOSE FIT')
    jean_sizes = models.CharField(max_length=4, choices=jean_sizes, default='M')
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    price = models.FloatField(default=0, blank=False)

    def __str__(self):
        return self.name
