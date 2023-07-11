from currency.models import ContactUs, Rate
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse as HR
from django.shortcuts import render # noqa

# Create your views here.


def index(request):
    return render(request, 'index.html')


def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HR(password)


def rate_list(request):
    rates = Rate.objects.all()

    context = {
        'rate_list': rates,
    }

    return render(request, 'rate_list.html', context=context)


def contact_us_list(request):
    contactus = ContactUs.objects.all()

    context = {
        'contactUs_lst': contactus,
    }

    return render(request, 'contactUs_list.html', context=context)


def response_codes(request):
    response = HR('Responce', status=301, headers={'Location': '/rate/list/'})
    return response
