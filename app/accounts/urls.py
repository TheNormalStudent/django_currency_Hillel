from django.urls import path
from accounts.views import MyProfileView

app_name = 'accounts'


urlpatterns = [
    path('my-profile/<int:pk>/', MyProfileView.as_view(), name='my-profile'),

]
