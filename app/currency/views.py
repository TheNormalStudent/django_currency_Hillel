from currency.forms import RateForm
from currency.models import ContactUs, Rate, Source
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse as HR, HttpResponseRedirect as HRR
from django.shortcuts import get_object_or_404, render # noqa

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

    return render(request, 'rate_front/rate_list.html', context=context)


def rate_create(request):
    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HRR('/rate/list/')
    elif request.method == "GET":
        form = RateForm()

    context = {
        'form': form
    }

    return render(request, 'rate_front/rate_create.html', context=context)


def rate_details(request, rate_id):

    # try:
    #     rate = Rate.objects.get(id=rate_id)
    # except Rate.DoesNotExist as exc:
    #     raise H404(exc)

    rate = get_object_or_404(Rate, id=rate_id)

    context = {
        'object': rate
    }

    return render(request, 'rate_front/rate_details.html', context=context)


def rate_update(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)

    if request.method == "POST":
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HRR('/rate/list/')
    elif request.method == "GET":
        form = RateForm(instance=rate)

    context = {
        'form': form,
        'rate_id': rate_id
    }

    return render(request, 'rate_front/rate_update.html', context=context)


def rate_delete(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id)

    if request.method == "POST":
        rate.delete()
        return HRR('/rate/list/')

    context = {
        'object': rate,
    }
    return render(request, 'rate_front/rate_delete.html', context=context)


def source_list(request):
    sources = Source.objects.all()

    context = {
        'source_list': sources,
    }

    return render(request, 'source_front/sources_list.html', context=context)

def contact_us_list(request):
    contactus = ContactUs.objects.all()

    context = {
        'contactUs_lst': contactus,
    }
    return render(request, 'contactUs_list.html', context=context)


def response_codes(request):
    response = HR('Responce', status=301, headers={'Location': '/rate/list/'})
    return response
