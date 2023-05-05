from django.db import models
from django.contrib.auth.models import AbstractUser
from . import choices as user_types


class User(AbstractUser):
    user_type = models.CharField(
        choices=user_types.USER_TYPES,
        max_length=8,
    )