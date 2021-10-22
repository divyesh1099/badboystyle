from django.db.models.fields import related
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request, name):
    product = Product.objects.get(name = name)
    related_products = Product.objects.filter(type=product.type).exclude(name=name)[:2]
    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, 'product/index.html', context)