from django.db.models.fields import related
from django.shortcuts import redirect, render
from .models import *
from cart.models import Item
# Create your views here.
def index(request, name):
    product = Product.objects.get(name = name)
    related_products = Product.objects.filter(type=product.type).exclude(name=name)[:2]
    if request.method == "POST":
        cart_product = request.POST["cart_product"]
        cart_item = Item.objects.create(name=cart_product)
        cart_item.save()
        print(Item.objects.all())
    else:
        context = {
            "product": product,
            "related_products": related_products,
        }
        return render(request, 'product/index.html', context)