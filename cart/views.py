from django.shortcuts import render
from .models import *
from product.models import *
from offer.models import Offer
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    items = Item.objects.all()
    subtotal = 0
    discount = 0
    shipping = 0
    total = 0
    for item in items:
        subtotal += (item.name.price * item.quantity)
        offered_items = Offer.objects.all()
        if item in offered_items:
            discount = offered_items.filter(name = item.name).discount
    total = subtotal-((subtotal)*discount)/100 + shipping
    
    # items = list()
    # for item in items_list:
        # items.append(Product.objects.get(name = item))
    context = {
        "items": items,
        # 'items_list':items_list
        "subtotal": subtotal,
        "discount": discount,
        "shipping": shipping,
        "total":total
    }
    return render(request, 'cart/index.html', context)