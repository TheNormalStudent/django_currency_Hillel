from accounts.views import ActivateUserView, MyProfileView, SignUpView

from django.urls import path

app_name = 'accounts'


urlpatterns = [
    path('my-profile/<int:pk>/', MyProfileView.as_view(), name='my-profile'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('activate/<uuid:username>/', ActivateUserView.as_view(), name='activate-user'),
]
