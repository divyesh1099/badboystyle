from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name = 'payment'

urlpatterns = [
    # path('', views.index, name = 'index'),
    path('payment_success', views.payment_success, name = 'payment_success'),
]