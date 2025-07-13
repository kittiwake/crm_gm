# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    tg_nickname = models.CharField(max_length=50, blank=True)
