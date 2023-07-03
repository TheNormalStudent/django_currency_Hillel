from django.shortcuts import render
from django.http import HttpResponse as HR
from currency.utils import generate_password as gen_pass

# Create your views here.


def hello_world(request):
    return HR('Hello world')

def generate_password(request):
    password_len = int(request.GET.get('password-len'))
    password = gen_pass(password_len)
    return HR(password)