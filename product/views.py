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
        # if request.POST['size']:
        #     size = request.POST['size']
        # if request.POST['color']:
        #     color = request.POST['color']
        # if request.POST['price']:
        #     new_price = request.POST['price']
        #     print(new_price)
        try:
            variation = request.POST['variation'].split(',')
            variation_size, variation_color,variation_variation, variation_price = str(variation[0].split("[")[1]), variation[1].strip(), variation[2].strip(), float(variation[3].split("]")[0].strip())
            new_size = Size.objects.get(size = variation_size)
            new_color = Color.objects.get(color = variation_color)
            new_price = variation_price
            new_product = Product.objects.get(name = cart_product)
            new_variation = variation_variation
            if new_product in Item.objects.all():
                Item.objects.filter(name = new_product).update(quantity = quantity)
                Item.objects.filter(name = new_product).update(size = str(new_size))
                Item.objects.filter(name = new_product).update(color = new_color)
                Item.objects.filter(name = new_product).update(price = new_price)
                Item.objects.filter(name = new_product).update(variation = new_variation)
            else:
                try:
                    Item.objects.update_or_create(name=new_product, defaults={'quantity': quantity})
                    Item.objects.filter(name=new_product).update(size = str(new_size), color = new_color, price = new_price, variation = variation_variation)
                except Exception as e:
                    print(e)
        except Exception as e:
            print("Variation Error is ", e)
        # if request.POST['variation']:
        #     variation = request.POST['variation'].split(',')
        #     variation_size, variation_color, variation_price = str(variation[0].split("[")[1]), variation[1].strip(), float(variation[2].split("]")[0].strip())
        #     new_size = Size.objects.get(size = variation_size)
        #     new_color = Color.objects.get(color = variation_color)
        #     new_price = variation_price
        #     print(variation_price)
        else:
            # if request.POST['size']:
            #     size = request.POST['size']
            # if request.POST['color']:
            #     color = request.POST['color']
            # if request.POST['price']:
            #     new_price = request.POST['price']
            #     print(new_price)
            # new_size = Size.objects.get(size = size)
            # new_color = Color.objects.get(color = color)
            pass
        # new_product = Product.objects.get(name = cart_product)
        # if new_product in Item.objects.all():
        #     Item.objects.filter(name = new_product).update(quantity = quantity)
        #     Item.objects.filter(name = new_product).update(size = str(new_size))
        #     Item.objects.filter(name = new_product).update(color = new_color)
        #     Item.objects.filter(name = new_product).update(price = new_price)
        # else:
        #     try:
        #         Item.objects.update_or_create(name=new_product, defaults={'quantity': quantity})
        #         Item.objects.filter(name=new_product).update(size = str(new_size), color = new_color)
        #     except Exception as e:
        #         print(e)
        return redirect('cart:index')
    else:
        return render(request, 'product/index.html', context)