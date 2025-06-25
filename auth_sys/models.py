from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Permissions(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODER = 'moderator', 'Модератор'

class Account(models.Model):
    image = models.ImageField(upload_to="auth_sys/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    birthday_day = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    permission = models.CharField(max_length=15, 
                                  choices=Permissions.choices, 
                                  default=Permissions.USER)
                                
    def __str__(self):
        return self.user.username
