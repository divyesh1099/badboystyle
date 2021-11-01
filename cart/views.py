from django.shortcuts import redirect, render
from .models import *
from product.models import *
from offer.models import Offer
from django.contrib.auth.decorators import login_required
import math
import razorpay

# Create your views here.

@login_required
def index(request):
    items = Item.objects.all()
    subtotal = 0
    discount_in_percent = 0
    shipping = 0
    total = 0
    try:
        offers = Offer.objects.all()
        for offer in offers:
            products = offer.product.all()
            for item in items:
                for product in products:
                    if str(item) == str(product):
                        max_discount = 0
                        if max_discount<offer.discount:
                            max_discount = offer.discount
                        discount_in_percent = max_discount      
    except:
        discount_in_percent = 0
    for item in items:
        subtotal += (item.name.price * item.quantity)
    discount = ((subtotal)*discount_in_percent)/100 
    total = math.ceil(subtotal- discount+ shipping)
    if total <1:
        total = 1
    total_in_paise = total*100
    context = {
        "items": items,
        "subtotal": subtotal,
        "discount": discount,
        "shipping": shipping,
        "total":total,
        "total_in_paise":total_in_paise,
    }

    if request.method == 'POST':
        client = razorpay.Client(auth=("rzp_test_C3J7evdYwRoSAs", "BcybRfQTm3EoB5fygqz2DihF"))
        DATA = {
            "amount": total,
            "currency": "INR",
        }
        client.order.create(data=DATA)
    return render(request, 'cart/index.html', context)

@login_required
def delete_item(request, item):
    try:
        product = Product.objects.get(name = item)
        Item.objects.get(name = product).delete()
    except Exception as e:
        print("Cannot delete because ", e)
    return redirect('cart:index')