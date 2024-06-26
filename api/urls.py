from django.urls import (
    path,
    include
)
from api import views


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"vendors", views.VendorViewSet)
router.register(r"purchase_orders", views.POViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("vendors/<str:vendor_id>/performance/",
         views.PerformanceViewSet.as_view({"get": "list"}), name="vendor-performance"),
    path("purchase_orders/<str:pk>/acknowledge/",
         views.POAckViewSet.as_view({"post": "update"}), name="acknowledge"),

]
