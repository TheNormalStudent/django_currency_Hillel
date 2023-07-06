from currency.views import contact_us_list, generate_password, hello_world, rate_list

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('generate-password/', generate_password),
    path('rate/list', rate_list),
    path('contactUs/list', contact_us_list)

]
