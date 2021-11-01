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
        quantity = request.POST['quantity']
        new_product = Product.objects.get(name = cart_product)
        if new_product in Item.objects.all():
            Item.objects.filter(name = new_product).update(quantity = quantity)
        else:
            try:
                cart_item = Item.objects.update_or_create(name=new_product, defaults={'quantity': quantity})
                cart_item[0].save()
            except Exception as e:
                print(e)
        return redirect('cart:index')
    else:
        context = {
            "product": product,
            "related_products": related_products,
        }
        return render(request, 'product/index.html', context)