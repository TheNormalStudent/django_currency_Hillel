from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task
def debug_task(sleep_time: int = 5):
    print("Starting debug") # noqa
    from time import sleep
    sleep(sleep_time)
    print(f'Task completed in {sleep_time}') # noqa


@shared_task
def contact_us(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )
