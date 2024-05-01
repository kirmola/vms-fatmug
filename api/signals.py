from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, Sum, F
from django.utils import timezone
from .models import Vendor, PurchaseOrder, Performance

@receiver(post_save, sender=PurchaseOrder)
def update_metrics(sender, instance, created, **kwargs):
    if instance.status == 'COMPLETED':
        vendor = instance.vendor

        # Calculate On-Time Delivery Rate
        completed_pos_count = PurchaseOrder.objects.filter(
            vendor=vendor, status='COMPLETED').count()
        on_time_deliveries_count = PurchaseOrder.objects.filter(
            vendor=vendor, status='COMPLETED', delivery_date__lte=timezone.now()).count()
        on_time_delivery_rate = (on_time_deliveries_count / completed_pos_count) * 100 if completed_pos_count != 0 else 0
        vendor.on_time_delivery_rate = on_time_delivery_rate

        # Calculate Quality Rating Average
        quality_rating_avg = PurchaseOrder.objects.filter(
            vendor=vendor, status='COMPLETED').exclude(quality_rating__isnull=True).aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        vendor.quality_rating_avg = quality_rating_avg

        # Calculate Fulfillment Rate
        vendors_total_purchase_order = PurchaseOrder.objects.filter(vendor=vendor)
        vendors_fulfilled_pos = vendors_total_purchase_order.filter(
            status='COMPLETED')
        fulfillment_rate = (vendors_fulfilled_pos.count() /
                            vendors_total_purchase_order.count()) * 100
        vendor.fulfillment_rate = fulfillment_rate

        # Calculate Average Response Time
        avg_response_time_timedelta = PurchaseOrder.objects.filter(vendor=vendor, status='COMPLETED').aggregate(
            avg_response_time=Avg(F('acknowledgement_date') - F('issue_date')))['avg_response_time']
        avg_response_time = (avg_response_time_timedelta.total_seconds()) / 60 if avg_response_time_timedelta else 0
        
        vendor.average_response_time = avg_response_time

        vendor.save()

        if created:
            # Calculate metrics for this vendor and date
            date = instance.delivery_date.date()

            total_completed_orders = PurchaseOrder.objects.filter(
                vendor=vendor, status='COMPLETED').count()
            on_time_delivery_count = PurchaseOrder.objects.filter(
                vendor=vendor, status='COMPLETED', delivery_date__lte=instance.delivery_date).count()
            on_time_delivery_rate = (on_time_delivery_count / total_completed_orders) * 100 if total_completed_orders != 0 else 0

            total_quality_ratings = PurchaseOrder.objects.filter(
                vendor=vendor, status='COMPLETED', quality_rating__isnull=False).count()
            quality_rating_sum = PurchaseOrder.objects.filter(
                vendor=vendor, status='COMPLETED', quality_rating__isnull=False).aggregate(
                sum_quality_rating=Sum('quality_rating'))['sum_quality_rating']
            quality_rating_avg = quality_rating_sum / total_quality_ratings

            total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
            total_fulfilled_orders = PurchaseOrder.objects.filter(
                vendor=vendor, status='COMPLETED').count()
            fulfillment_rate = (total_fulfilled_orders / total_orders) * 100

            # Update or create Performance record
            Performance.objects.update_or_create(
                vendor=vendor,
                date=date,
                defaults={
                    'on_time_delivery_rate': on_time_delivery_rate,
                    'avg_response_time': avg_response_time,
                    'quality_rating_avg': quality_rating_avg,
                    'fulfillment_rate': fulfillment_rate
                }
            )
