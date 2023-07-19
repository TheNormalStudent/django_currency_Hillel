from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse as HR, HttpResponseRedirect as HRR
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from django.shortcuts import get_object_or_404, render # noqa

# Create your views here.

# def index(request): #the same as IndexView class
#     return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'


# def generate_password(request):
#     password_len = int(request.GET.get('password-len'))
#     password = gen_pass(password_len)
#     return HR(password)

# class View is used when you need to use your own code and mostly don`t want to have connection to parent class.
# Used when there are only classes in Views and you don`t want to change format and how code looks


class GeneratePasswordView(View):
    def get(self, request):
        password_len = int(request.GET.get('password-len'))
        password = gen_pass(password_len)
        return HR(password)


class GeneratePasswordBView(TemplateView):
    template_name = 'generate_password.html'

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)

        password_len = int(self.request.GET.get('password-len'))
        context['password'] = gen_pass(password_len)

        return context


# def rate_list(request): # does the same as the RateListView class
#     rates = Rate.objects.all()

#     context = {
#         'rate_list': rates,
#     }

#     return render(request, 'rate_front/rate_list.html', context=context)


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_front/rate_list.html'


# def rate_create(request): # does the same as the RateCreateView class
#     if request.method == "POST":
#         form = RateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HRR('/rate/list/')
#     elif request.method == "GET":
#         form = RateForm()

#     context = {
#         'form': form
#     }

#     return render(request, 'rate_front/rate_create.html', context=context)


class RateCreateView(CreateView):
    model = Rate  # or queryset = Rate.object.all() if you want some accurate set
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')  # redirect place
    template_name = 'rate_front/rate_create.html'


# def rate_details(request, rate_id):

#     # try: # the same as get_object_or_404(Rate, id = rate_id)
#     #     rate = Rate.objects.get(id=rate_id)
#     # except Rate.DoesNotExist as exc:
#     #     raise H404(exc)

#     rate = get_object_or_404(Rate, id=rate_id)

#     context = {
#         'object': rate
#     }

#     return render(request, 'rate_front/rate_details.html', context=context)


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_front/rate_details.html'

# def rate_update(request, rate_id): # does the same as RateUpdateView(UpdateView)
#     rate = get_object_or_404(Rate, id=rate_id)

#     if request.method == "POST":
#         form = RateForm(request.POST, instance=rate)
#         if form.is_valid():
#             form.save()
#             return HRR('/rate/list/')
#     elif request.method == "GET":
#         form = RateForm(instance=rate)

#     context = {
#         'form': form,
#         'rate_id': rate_id
#     }

#     return render(request, 'rate_front/rate_update.html', context=context)


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')  # redirect place
    template_name = 'rate_front/rate_update.html'

# def rate_delete(request, rate_id): # the same as RateDeleteView class
#     rate = get_object_or_404(Rate, id=rate_id)

#     if request.method == "POST":
#         rate.delete()
#         return HRR('/rate/list/')

#     context = {
#         'object': rate,
#     }
#     return render(request, 'rate_front/rate_delete.html', context=context)


class RateDeleteView(DeleteView):
    model = Rate
    success_url = '/rate/list/'
    template_name = 'rate_front/rate_delete.html'


def source_create(request):
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HRR('/source/list/')
    elif request.method == "GET":
        form = SourceForm()

    context = {
        'form': form,
    }

    return render(request, 'sources_front/sources_create.html', context=context)


def source_list(request):
    sources = Source.objects.all()

    context = {
        'source_list': sources,
    }

    return render(request, 'sources_front/sources_list.html', context=context)


def source_update(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    if request.method == "POST":
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HRR('/source/list/')
    elif request.method == "GET":
        form = SourceForm(instance=source)

    context = {
        'form': form,
        'source_id': source_id
    }

    return render(request, 'sources_front/source_update.html', context=context)


def source_delete(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    if request.method == "POST":
        source.delete()
        return HRR('/source/list/')

    context = {
        'object': source,
    }
    return render(request, 'sources_front/source_delete.html', context=context)


def source_details(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    context = {
        'object': source
    }

    return render(request, 'sources_front/source_details.html', context=context)


def contact_us_list(request):
    contactus = ContactUs.objects.all()

    context = {
        'contactUs_lst': contactus,
    }
    return render(request, 'contactUs_list.html', context=context)


def response_codes(request):
    response = HR('Responce', status=301, headers={'Location': '/rate/list/'})
    return response
