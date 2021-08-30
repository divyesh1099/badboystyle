from django.urls import path
from . import views
app_name = 'shirt'
urlpatterns = [
    path('', views.index, name = 'index'),
]