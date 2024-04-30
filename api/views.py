from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, PurchaseOrder, Performance
from .serializers import VendorSerializer

class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    http_method_names = ["get", "post"]

# class POViewSet(ModelViewSet):
#     pass