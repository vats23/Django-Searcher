from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.location
