from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid


class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

