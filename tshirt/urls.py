from django.urls import path
from . import views
app_name = 'tshirt'
urlpatterns = [
    path('', views.index, name = 'index'),
]