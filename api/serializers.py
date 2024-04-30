from rest_framework.serializers import ModelSerializer
from .models import Vendor, PurchaseOrder, Performance


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class POSerializer(ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"