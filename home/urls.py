from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('all', views.all, name= 'all'),
    path('login', views.my_login, name= 'login'),
    path('logout', views.my_logout, name= 'logout'),
    path('signup', views.my_signup, name = 'signup'),
    path('gallery', views.gallery, name= 'gallery'),
    path('categories', views.categories, name = 'categories'),
    ]