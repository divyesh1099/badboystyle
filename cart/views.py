from django.shortcuts import render
from .models import *
# Create your views here.
items = Item.objects.all()
def index(request):
    context = {
        "items": items,
    }
    return render(request, 'cart/index.html', context)