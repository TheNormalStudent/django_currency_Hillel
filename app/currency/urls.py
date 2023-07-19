from currency.views import (
    GeneratePasswordBView, GeneratePasswordView,
    RateCreateView, RateDeleteView, RateDetailView, RateListView, RateUpdateView,
    contact_us_list,
    response_codes,
    source_create, source_delete, source_details, source_list, source_update,
    )

from django.urls import path

app_name = 'currency'

# if you want to use view func instead of view class
# you shouldn`t use command .as_view() just write down the name of view func

urlpatterns = [

    # currency
    path('generate-password/', GeneratePasswordView.as_view()),
    path('generate-password-b/', GeneratePasswordBView.as_view()),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('source/create/', source_create),
    path('source/list/', source_list),
    path('source/update/<int:source_id>/', source_update),
    path('source/delete/<int:source_id>/', source_delete),
    path('source/details/<int:source_id>/', source_details),
    path('contactUs/list/', contact_us_list),
    path('response-codes/', response_codes),
]
