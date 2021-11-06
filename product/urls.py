from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('<str:name>', views.index, name = 'index'),
    path('review/<str:name>', views.review, name = 'review'),
    path('comment/<str:name>', views.comment, name = 'comment'),
    path('comment/<str:name>/<str:comment_id>', views.delete_comment, name = 'delete_comment'),
]

