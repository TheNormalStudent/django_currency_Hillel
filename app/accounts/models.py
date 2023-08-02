from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        default=None
    )

    email = models.EmailField(
        'email adress', blank=False, null=False, unique=True,
    )
    