from rest_framework import generics, permissions,filters
from .serializers import flysserializer, companySerializer
from main.models import Flyings, Company


class flysList(generics.ListAPIView):
    search_fields = ['fr', 'to', 'wh']
    filter_backends = (filters.SearchFilter,)
    serializer_class = flysserializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Flyings.objects.all().order_by('price')


class Companylist(generics.ListAPIView):
    serializer_class = companySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Company.objects.all()
