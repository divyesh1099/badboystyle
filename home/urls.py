from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('all', views.all, name= 'all'),
    path('gallery', views.gallery, name= 'gallery'),
    ]