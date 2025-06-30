from django.db import models
from django.contrib.auth.models import User
from app.preferences import PREFERENCES, GENDER, INTRESRED_IN
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=100, choices=GENDER, blank=True, null=True)
    intrested_in = models.CharField(max_length=100, choices=INTRESRED_IN, blank=True, null=True)
    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    
class Preferences(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='preferences')
    preferences = models.CharField(choices=PREFERENCES, max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email}'s Preferences"