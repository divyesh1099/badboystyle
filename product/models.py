from django.db import models
from django.db.models.fields.related import ForeignKey

sizes = [
    ('36', '36'),
    ('38', '38'),
    ('40', '40'),
    ('42', '42'),
    ('44', '44'),
    ('46', '46'),
    ('48', '48'),
    ('50', '50'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
]


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length = 100, blank=True, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    size = models.CharField(max_length=4, choices=sizes)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    stock = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    price = models.FloatField(default=0)

    class Meta:
        ordering = ['edited']

    def __str__(self):
        return self.name
