from django.urls import path
from . import views
app_name = 'review'

urlpatterns = [
    path('<str:name>', views.index, name = 'index'),
    path('delete/<str:name>', views.delete_review, name = 'delete_review'),
]