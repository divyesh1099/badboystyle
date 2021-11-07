from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from colorfield.fields import ColorField

# Create Your Models Here

class Size(models.Model):
    size = models.CharField(max_length=1000, blank=True, unique=True)

    class Meta:
        ordering = ['size']
    
    def __str__(self):
        return self.size

class Color(models.Model):
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red"),
        ("#FFFF00", "yellow"),
        ("#0000FF", "blue"),
        ("#00FF00", "green"),
        ("#808080", "grey"),
        ("#800000", "maroon"),
    ]
    color = ColorField(default = '#FF0000', choices = COLOR_CHOICES)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length = 100, blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'types/')
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name

class Specification(models.Model):
    product_dimension_LxWxH = models.CharField(max_length = 200, blank=True, null=True)
    date_first_available = models.DateField(auto_now_add=True, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=200, blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True, default='PRODUCT')
    manufacturer_address = models.CharField(max_length=500, blank=True, null=True)
    packer_address = models.CharField(max_length=500, blank=True, null=True)
    item_weight = models.FloatField(blank=True, null=True)
    net_quantity = models.IntegerField(blank=True, null=True)
    included_components = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['department']

    def __str__(self):
        return self.department


class Product(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="type_of_product")
    sizes_available = models.ManyToManyField(Size, related_name="size_available_of_sizes", blank=True)
    colors_available = models.ManyToManyField(Color, related_name="colors_available_of_color", blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    image2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank = True, null = True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d/', blank = True, null = True)
    description = models.TextField()
    detail = models.TextField()
    specification = models.OneToOneField(Specification, on_delete=models.CASCADE, related_name="specification_of_product", blank=True, null=True)
    stock = models.PositiveBigIntegerField(default=1)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    price = models.FloatField(default=0)
    rating = models.SmallIntegerField(blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    generated_product_id = models.CharField(max_length=100,  default=uuid.uuid4, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['edited']

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_of_product', blank=True)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.author.username