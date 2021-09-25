from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # watchlist=models.ForeignKey(Watchlist, related_name="watchlistofuser", blank=True, on_delete=models.CASCADE)
    pass