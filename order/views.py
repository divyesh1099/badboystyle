from django.db.models.query_utils import PathInfo
from django.shortcuts import render
from cart.models import Item
from django.contrib.auth.decorators import login_required
from .models import Order, Total
# Create your views here.

@login_required
def index(request):
    total = Total.objects.all().last()
    items = Item.objects.all()
    if request.method == "POST":
        user = request.user
        phonenumber = request.POST["phonenumber"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zip"]
        amount = total
        dispatched = False
        delivered = False
        paid = False
        try:
            new_order = Order.objects.create(user = user,phonenumber = phonenumber, address = address, city = city, state = state, zip = zip_code, amount = amount, dispatched = dispatched, delivered = delivered, paid = paid)
            for product in items:
                new_order.products.add(product.name.id)
            new_order.save()
            print("New order amount", new_order.amount)
        except Exception as e:
            print("The following error occured", e)
        order = new_order
        print("Order ", order)
        items = Item.objects.all()
        total_in_paise = order.amount.total *100
        context = {
            "order": order,
            "items": items,
            "total_in_paise": total_in_paise,
        }
        return render(request, 'payment/index.html', context)

    return render(request, 'order/index.html')

@login_required
def history(request):
    orders = Order.objects.filter(user = request.user)
    context = {
        "orders": orders,
    }
    return render(request, 'order/history.html', context)