from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.conf import settings
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

# class UserModel(User):
#     pass

class Type(models.Model):
    name = models.CharField(max_length = 100, blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'types/')
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.author.username

class Specification(models.Model):
    product_dimension_LxWxH = models.CharField(max_length = 200, blank=True, null=True)
    date_first_available = models.DateField(auto_now_add=True, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=200, blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    manufacturer_address = models.CharField(max_length=500, blank=True, null=True)
    packer_address = models.CharField(max_length=500, blank=True, null=True)
    item_weight = models.FloatField(blank=True, null=True)
    net_quantity = models.IntegerField(blank=True, null=True)
    included_components = models.TextField(blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="type_of_product")
    size = models.CharField(max_length=4, choices=sizes)
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
    comment = models.ManyToManyField(Comment, blank=True)

    class Meta:
        ordering = ['edited']

    def __str__(self):
        return self.name