from django.shortcuts import render
from django.views.generic import UpdateView

from accounts.models import User
from django.urls import reverse_lazy

# Create your views here.

class MyProfileView(UpdateView):
    queryset = User.objects.all()
    fields = (
        'first_name',
        'last_name'
    )

    success_url = reverse_lazy('index')
    template_name = 'my_profile.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id = self.request.user.id)
    #     return queryset

    def get_object(self, queryset=None):
        return self.request.user