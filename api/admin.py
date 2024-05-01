from django.contrib import admin
from django.http import HttpRequest

from .models import (
    PurchaseOrder,
    Vendor,
    Performance
)


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    readonly_fields = (
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate"
    )     # These fields can't be changed from admin dashboard, they will be updated automatically, on the basis of Ratings


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
