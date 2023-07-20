from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.utils import generate_password as gen_pass

from django.http import HttpResponse as HR
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from django.shortcuts import get_object_or_404, render # noqa


class IndexView(TemplateView):
    template_name = 'index.html'


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


# Rate CRUD + Details


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_front/rate_list.html'


class RateCreateView(CreateView):
    model = Rate  # or queryset = Rate.object.all() if you want some accurate set
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')  # redirect place
    template_name = 'rate_front/rate_create.html'


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_front/rate_details.html'


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')  # redirect place
    template_name = 'rate_front/rate_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_front/rate_delete.html'


# Source CRUD + Details

class SourceCreateView(CreateView):
    model = Source  # or queryset = Rate.object.all() if you want some accurate set
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')  # redirect place
    template_name = 'sources_front/source_create.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'sources_front/source_list.html'


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')  # redirect place
    template_name = 'sources_front/source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'sources_front/source_delete.html'


class SourceDetailView(DetailView):
    queryset = Source.objects.all()
    template_name = 'sources_front/source_details.html'


def contact_us_list(request):
    contactus = ContactUs.objects.all()

    context = {
        'contactUs_lst': contactus,
    }
    return render(request, 'contactUs_list.html', context=context)


def response_codes(request):
    response = HR('Responce', status=301, headers={'Location': '/rate/list/'})
    return response
