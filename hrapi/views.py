from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Professional
from .serializers import ProfessionalSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProfessionalList(generics.ListCreateAPIView):
    serializer_class = ProfessionalSerializer
    queryset = Professional.objects.all()
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'
    ordering_fields = '__all__'


class ProfessionalDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfessionalSerializer
    queryset = Professional.objects.all()

