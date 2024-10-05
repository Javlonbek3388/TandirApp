from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username', 'programming_language']
    ordering = ['created_at']

