from currency.views import contact_us_list, generate_password, index, rate_list, response_codes

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('generate-password/', generate_password),
    path('rate/list/', rate_list),
    path('contactUs/list/', contact_us_list),
    path('response-codes/', response_codes),

]
