from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.tasks import contact_us
from currency.utils import generate_password as gen_pass


# from django.conf import settings
# from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse as HR, JsonResponse as JR
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View


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
    queryset = Rate.objects.all().select_related('source').order_by('-created')
    template_name = 'rate_front/rate_list.html'


class RateCreateView(CreateView):
    model = Rate  # or queryset = Rate.object.all() if you want some accurate set
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')  # redirect place
    template_name = 'rate_front/rate_create.html'


class RateDetailView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_front/rate_details.html'


class RateUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')  # redirect place
    template_name = 'rate_front/rate_update.html'

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_front/rate_delete.html'

    def test_func(self):
        return self.request.user.is_superuser


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


class ContactUsCreateView(CreateView):
    model = ContactUs
    success_url = reverse_lazy('index')
    template_name = 'contactus_create.html'
    fields = (
        'email_to',
        'subject',
        'body'
    )

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        email_to = form.cleaned_data['email_to']

        full_email_body = f'''
        Email from: {email_to}
        Body: {body}
        '''

        contact_us.apply_async(args=(subject, ), kwargs={'body': full_email_body})

        return super().form_valid(form)


def contact_us_list(request):
    contactus = ContactUs.objects.all()

    context = {
        'contactUs_list': contactus,
    }
    return render(request, 'contactUs_list.html', context=context)


def response_codes(request):
    response = HR('Responce', status=301, headers={'Location': '/rate/list/'})
    return response
