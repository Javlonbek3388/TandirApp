from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    full_name = models.CharField(max_length=55)
    username = models.CharField(max_length=70, unique=True)
    programming_language = models.CharField(max_length=55)
    photo = models.ImageField(upload_to='user/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'heic', 'heif'])
    ])
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    win_count = models.IntegerField(default=0)
    lose_count = models.IntegerField(default=0)
