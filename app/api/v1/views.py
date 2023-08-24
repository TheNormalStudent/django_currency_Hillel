from rest_framework import viewsets

from api.v1.paginators import RatePagination
from api.v1.serializers import RateSerializer

from currency.models import Rate

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = RatePagination
