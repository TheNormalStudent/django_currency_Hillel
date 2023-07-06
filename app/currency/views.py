from currency.models import ContactUs, Rate
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse as HR
from django.shortcuts import render # noqa

# Create your views here.


def hello_world(request):
    return HR('Hello world')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HR(password)


def rate_list(request):
    rates = Rate.objects.all()

    result = []
    for rate in rates:
        result.append(f'Rate: {rate.id} Sale: {rate.sale} Buy: {rate.buy} </br>')

    return HR(str(result))


def contact_us_list(request):
    conctactus = ContactUs.objects.all()

    result = []
    for item in conctactus:
        result.append(
            f'ID: {item.id} Email: {item.email_from} Subject: {item.subject} Message: {item.message} </br>'
            )

    return HR(str(result))
