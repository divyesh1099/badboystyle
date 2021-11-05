from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pictures/')
    phonenumber = models.PositiveBigIntegerField(blank = True, default=0000000000)
    country = models.CharField(max_length = 100, blank = True, default="India")
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username