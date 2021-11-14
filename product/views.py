from django import utils
from django.db.models.fields import related
from django.http.request import MediaType
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from cart.models import Item
from offer.models import Offer
# Create your views here.
def index(request, name):
    product = Product.objects.get(name = name)
    comments = Comment.objects.all().filter(product=product)
    related_products = Product.objects.filter(type=product.type).exclude(name=name)[:2]
    discount = 0
    offers = Offer.objects.all()
    for offer in offers:
        if product in offer.product.all():
            discount = offer.discount
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
        context = {
            "product": product,
            "related_products": related_products,
            "comments":comments,
            "discount":discount,
        }
    return render(request, 'product/index.html', context)

@login_required
def comment(request, name):
    product = Product.objects.get(name = name)
    comments = Comment.objects.all().filter(product=product)
    related_products = Product.objects.filter(type=product.type).exclude(name=name)[:2]
    context = {
            "product": product,
            "related_products": related_products,
            "comments":comments,
        }
    if request.method == "POST":
        if request.POST['comment']:
            comment = request.POST['comment']
            product = Product.objects.get(name = name)
            new_comment = Comment.objects.create(comment = comment, author = request.user, product = product)
            new_comment.save()
        else:
            pass
        return render(request, 'product/index.html', context)
    
    return render(request, 'product/index.html', context)

@login_required
def delete_comment(request, name, comment_id):
    try:
        Comment.objects.filter(pk = comment_id).delete()
    except Exception as e:
        print("Cannot Delete because", e)
    product = Product.objects.get(name = name)
    comments = Comment.objects.all().filter(product=product)
    related_products = Product.objects.filter(type=product.type).exclude(name=name)[:2]
    context = {
        "product": product,
        "related_products": related_products,
        "comments":comments,
    }
    return render(request, 'product/index.html', context)

def review(request, name):
    return render(request, 'product/review.html')