from rest_framework import viewsets, generics
from rest_framework.response import Response

from api.v1.paginators import RatePagination, SourcePagination, ContactUsPagination
from api.v1.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from api.v1.filters import RateFilter
from api.v1.throttles import AnonUserRateThrottle

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency.models import Rate, Source, ContactUs
from currency import choices as ch

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('source')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'created', 'sale', 'buy']
    throttle_classes = [AnonUserRateThrottle]

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    pagination_class = ContactUsPagination
    # filterset_class = ContactUsFilter
    filter_backends = [
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    ]
    search_fields = ['email_to', 'subject', 'body']
    ordering_fields = ['subject']


class RateChoicesView(generics.GenericAPIView):
    def get(self, request):
        return Response(
            {'rate_types': ch.RATE_TYPES},
            )


class SourceListView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    pagination_class = SourcePagination

