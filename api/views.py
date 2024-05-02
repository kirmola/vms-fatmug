from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, PurchaseOrder, Performance
from .serializers import (
    VendorSerializer,
    POSerializer, 
    PerformanceSerializer,
    POAckSerializer
    )
from datetime import datetime
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from api.signals import ack_signal

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


class PerformanceViewSet(ModelViewSet):
    serializer_class = PerformanceSerializer
    http_method_names = ["get"]    
    
    
    def get_queryset(self):
        vendor_id = self.kwargs.get("vendor_id")
        return get_list_or_404(Performance, vendor=vendor_id)
    
class POAckViewSet(ModelViewSet):
    serializer_class = POAckSerializer
    http_method_names = ["patch"]
    queryset = PurchaseOrder.objects.all()
        
    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        response = super().update(request, *args, **kwargs)    
        ack_signal.send(sender=self.__class__, instance=self.get_object())
        return response