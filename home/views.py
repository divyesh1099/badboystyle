from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def all(request):
    return render(request, 'home/all.html')

def gallery(request):
    return render(request, 'home/gallery.html')