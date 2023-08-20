from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializer import AdSerializer, MarkaSerializer
from api.models import Ad
# Create your views here.


class AdViewSet(ReadOnlyModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
