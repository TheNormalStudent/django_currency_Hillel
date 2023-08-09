from currency import choices as ch

from django.db import models

# Create your models here.

def upload_source_avatar(instance, filename):
    return f'source_avatars/{instance.id}/{filename}'


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)  # 123.45
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)  # examples: privatbank, monobank
    type = models.CharField(max_length=3, choices=ch.RATE_TYPES)  # noqa examples: USD, EUR


class ContactUs(models.Model):
    email_to = models.EmailField(max_length=48)
    subject = models.CharField(max_length=32)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Source(models.Model):
    source_url = models.CharField(max_length=256)
    name = models.CharField(max_length=64)

    source_avatar = models.FileField(
        upload_to=upload_source_avatar,
        blank=True,
        null=True,
        default=None,
    )


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=255)
    response_time = models.PositiveSmallIntegerField()
    request_method = models.CharField(max_length=8, choices=ch.REQUEST_METHOD_TYPES)
