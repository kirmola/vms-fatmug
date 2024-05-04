from rest_framework.viewsets import ModelViewSet
from .models import (
    Vendor,
    PurchaseOrder,
    Performance
)
from .serializers import (
    VendorSerializer,
    POSerializer,
    PerformanceSerializer,
    POAckSerializer
)
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_list_or_404
from api.signals import ack_signal


class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = VendorSerializer
    http_method_names = ["get", "post", "put", "delete",
                         "patch"]   # patch added for testing only


class POViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = POSerializer
    http_method_names = ["get", "post", "put", "delete",
                         "patch"]   # patch added for testing only
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["vendor"]


class PerformanceViewSet(ModelViewSet):
    serializer_class = PerformanceSerializer
    http_method_names = ["get"]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        vendor_id = self.kwargs.get("vendor_id")
        return get_list_or_404(Performance, vendor=vendor_id)


class POAckViewSet(ModelViewSet):
    serializer_class = POAckSerializer
    http_method_names = ["post"]
    queryset = PurchaseOrder.objects.all()
    authentication_classes = [TokenAuthentication]
