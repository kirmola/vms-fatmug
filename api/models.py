from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)


class Vendor(models.Model):

    name = models.CharField(_("Vendor's Name"), max_length=75)
    contact_details = models.TextField(_("Vendor's Contact Information"))
    address = models.TextField(_("Vendor's Physical Address"))
    vendor_code = models.CharField(
        _("Vendor's Unique Identifier"), max_length=50, primary_key=True)
    on_time_delivery_rate = models.FloatField(_("Percentage of On-time delivery"), validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=100)
    ], default=None, null=True)   # 0-100 percentage-range
    quality_rating_avg = models.FloatField(_("Quality Rating"), validators=[
        MinValueValidator(limit_value=1),   # Rating not below 1
        MaxValueValidator(limit_value=5),   # Rating no more than 5
    ], default=None, null=True)
    average_response_time = models.FloatField(
        _("Average Response time of vendor"), default=None, null=True)
    fulfillment_rate = models.FloatField(_("Order Fulfillment rate of vendor"), validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=100)
    ], default=None, null=True)

    class Meta:
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Vendor_detail", kwargs={"vendor_id": self.vendor_code})


class PurchaseOrder(models.Model):

    ORDER_STATUS = {
        "PENDING": "Pending",
        "COMPLETED": "Completed",
        "CANCELLED": "Cancelled",
    }

    po_number = models.CharField(
        _("Unique PO Number"), max_length=50, primary_key=True)
    vendor = models.ForeignKey("api.Vendor", verbose_name=_(
        "Vendor"), on_delete=models.CASCADE)
    order_date = models.DateTimeField(_("Order Date"), auto_now_add=True)
    delivery_date = models.DateTimeField(_("Delivery Date"), auto_now=True)
    items = models.JSONField(_("Ordered Items Details"), default=dict)
    quantity = models.IntegerField(_("Quantity of Items"))
    status = models.CharField(
        _("Order Status"), choices=ORDER_STATUS, max_length=50)
    quality_rating = models.FloatField(_("Quality Rating of Order"), default=None, validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=5),
    ])
    issue_date = models.DateTimeField(
        _("Order Issue Date to the Vendor"), default=None)
    acknowledgement_date = models.DateTimeField(
        _("Order Acknowledgment Date"), default=None)

    class Meta:
        verbose_name = _("Purchase Order")
        verbose_name_plural = _("Purchase Orders")

    def __str__(self):
        return f"Purchase ID: '{self.po_number}', Vendor: {self.vendor}"

    def get_absolute_url(self):
        return reverse("PurchaseOrder_detail", kwargs={"po_id": self.po_number})


class Performance(models.Model):

    vendor = models.ForeignKey("api.Vendor", verbose_name=_(
        "Vendor"), on_delete=models.CASCADE)
    date = models.DateField(_("Date of Performace Record"),
                            auto_now=True)
    on_time_delivery_rate = models.FloatField(_("Percentage of On-time delivery"), validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=100)
    ], default=None)
    avg_response_time = models.FloatField(
        _("Average Response time in Minutes"), default=None)
    quality_rating_avg = models.FloatField(_("Average Quality Rating"), validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=5)
    ], default=None)
    fulfillment_rate = models.FloatField(_("Order Fulfillment rate of vendor"), validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=100)
    ], default=None)

    class Meta:
        verbose_name = _("Performance")
        verbose_name_plural = _("Performance Detail")

    def __str__(self):
        return f"Performace Report of {self.vendor} on {self.date}"

    def get_absolute_url(self):
        return reverse("Performance_detail", kwargs={"vendor_id": self.vendor})
