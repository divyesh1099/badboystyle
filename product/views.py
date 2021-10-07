from django.shortcuts import render
from .models import *
# Create your views here.
def index(request, name):
    product = Product.objects.get(name = name)
    context = {
        "product": product,
    }
    return render(request, 'product/index.html', context)