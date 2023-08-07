from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


def upload_avatar(instance, filename):
    return f'avatars/{instance.id}/{filename}'


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    avatar = models.FileField(
        upload_to=upload_avatar,
        blank=True,
        null=True,
        default=None,
    )

    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        default=None
    )

    email = models.EmailField(
        'email adress', blank=False, null=False, unique=True,
    )
