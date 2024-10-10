from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from rest_framework_simplejwt.tokens import RefreshToken

from base.enum import Tillar
from base.models import BaseModel


class User(BaseModel, AbstractUser):
    name = models.CharField(max_length=55)
    programming_language = models.CharField(max_length=255, choices=Tillar.choices())
    photo = models.ImageField(upload_to='user/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'heic', 'heif'])
    ])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game_count = models.IntegerField(default=0)
    win_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    lose_count = models.IntegerField(default=0)
