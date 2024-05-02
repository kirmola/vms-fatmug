"""
URL configuration for vms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r"vendors", views.VendorViewSet)
router.register(r"purchase_orders", views.POViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/vendors/<str:vendor_id>/performance/", views.PerformanceViewSet.as_view({"get":"list"}), name="vendor_performance"),
    path("api/purchase_orders/<str:pk>/acknowledge/", views.POAckViewSet.as_view({"patch":"partial_update"})),
    path("auth/", include("rest_framework.urls"))
]
