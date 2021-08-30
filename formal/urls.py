from django.urls import path 
from . import views
app_name = 'formal'
urlpatterns = [
    path('', views.index, name = 'index'),
]