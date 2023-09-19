from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.v1 import views

app_name = 'api'

router = DefaultRouter()
router.register(r'rates', views.RateViewSet, basename='rate')
router.register(r'contactUs', views.ContactUsViewSet, basename='contactUs')

urlpatterns = [
    path('sources/', views.SourceListView.as_view(), name='source'),
    path('choices/', views.RateChoicesView.as_view(), name='choices'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns.extend(router.urls)