from django.db import models

# Create your models here.


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)  # 123.45
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)  # examples: privatbank, monobank
    type = models.CharField(max_length=3)  # noqa examples: USD, EUR


class ContactUs(models.Model):
    email_to = models.EmailField(max_length=48)
    subject = models.CharField(max_length=32)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Source(models.Model):
    source_url = models.CharField(max_length=256)
    name = models.CharField(max_length=64)
