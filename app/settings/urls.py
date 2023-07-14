from currency.views import (
    contact_us_list,
    generate_password,
    index,
    rate_create, rate_delete, rate_details, rate_list, rate_update,
    response_codes
    )

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('generate-password/', generate_password),
    path('rate/create/', rate_create),
    path('rate/list/', rate_list),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/delete/<int:rate_id>/', rate_delete),
    path('contactUs/list/', contact_us_list),
    path('response-codes/', response_codes),
]
