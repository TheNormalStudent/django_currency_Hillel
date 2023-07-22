from currency.views import (
    ContactUsCreateView,
    GeneratePasswordBView, GeneratePasswordView,
    RateCreateView, RateDeleteView, RateDetailView, RateListView, RateUpdateView,
    SourceCreateView, SourceDeleteView, SourceDetailView, SourceListView, SourceUpdateView,
    contact_us_list,
    response_codes,
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

    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-details'),

    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),

    path('contactUs/list/', contact_us_list),
    path('response-codes/', response_codes),
]
