from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, PurchaseOrder, Performance
from .serializers import VendorSerializer, POSerializer
from django_filters.rest_framework import DjangoFilterBackend

class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    http_method_names = ["get", "post", "put", "delete"]

class POViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = POSerializer
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["vendor"]