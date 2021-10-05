from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.db import IntegrityError
from product.models import *
from .models import *
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    carousel_images = CarouselImage.objects.get()
    featured_list = Featured.objects.all()
    featured = list()
    for feature in featured_list:
        featured.append(Product.objects.get(name = feature))
    context = {
        'carousel_images': carousel_images,
        'featured': featured
        }
    return render(request, 'home/index.html', context)

def all(request):
    products = Product.objects.all()
    categories = Type.objects.all()
    sizes = ['36','38','40','42','44','46','48','50','S','M','L','XL','XXL','XXXL']
    context = {
        "products": products,
        "categories": categories,
        "sizes":sizes,
    }
    return render(request, 'home/all.html', context)

def gallery(request):
    gallery_list = Gallery.objects.all()
    gallery = list()
    for gallerie in gallery_list:
        gallery.append(Product.objects.get(name = gallerie))
    context = {
        'gallery': gallery
        }
    return render(request, 'home/gallery.html', context)

def categories(request):
    categories = Type.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'home/categories.html', context)

def category(request, category):
    categorie = get_object_or_404(Type, name = category)
    products = Product.objects.filter(type = categorie.id)
    context = {
        'category': categorie,
        'products': products,
    }
    return render(request, 'home/category.html', context)

def my_login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return render(request, 'home/index.html', {'success': "Logged in Successfully"})
        else:
            return render(request, "home/login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")

def my_logout(request):
    logout(request)
    return render(request, 'home/index.html', {'success': "Logged Out Successfully"})

def my_signup(request):
    customer_group = Group.objects.get(name='Customer')
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password1"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "home/signup.html", {
                "error": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
            user.is_active=True
            user.is_staff=True
            customer_group.user_set.add(user)
            user.save()
        except IntegrityError:
            print("Error")
            return render(request, "home/signup.html", {
                "error": "Username already taken."
            })
        login(request, user)
        return render(request, 'home/index.html', {"success": "Logged In Successfully"})
    else:
        return render(request, "home/signup.html")