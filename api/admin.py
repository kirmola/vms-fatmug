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
    pass    

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
