from django import utils
from django.db.models.fields import related
from django.http.request import MediaType
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from cart.models import Item

# Create your views here.
def index(request, name):
    product = Product.objects.get(name = name)
    try:
        related_products = Product.objects.filter(type=product.type).exclude(name=name)[:2]
        context = {
            "product": product,
            "related_products": related_products,
        }
    except Exception as e:
        print("The Review Finding Error is ", e)

    if request.method == "POST":
        cart_product = request.POST["cart_product"]
        quantity = request.POST['quantity']
        size = request.POST['size']
        color = request.POST['color']
        new_product = Product.objects.get(name = cart_product)
        new_size = Size.objects.get(size = size)
        new_color = Color.objects.get(color = color)
        if new_product in Item.objects.all():
            Item.objects.filter(name = new_product).update(quantity = quantity)
            Item.objects.filter(name = new_product).update(size = size)
            Item.objects.filter(name = new_product).update(color = color)
        else:
            try:
                Item.objects.update_or_create(name=new_product, defaults={'quantity': quantity})
                Item.objects.filter(name=new_product).update(size = size, color = new_color)
            except Exception as e:
                print(e)
        return redirect('cart:index')
    else:
        return render(request, 'product/index.html', context)