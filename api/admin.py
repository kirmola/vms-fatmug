from django.contrib import admin

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
    pass
