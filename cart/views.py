from django.shortcuts import render
from .models import *
from product.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    items_list = Item.objects.all()
    items = list()
    for item in items_list:
        items.append(Product.objects.get(name = item))
    context = {
        "items": items,
    }
    return render(request, 'cart/index.html', context)