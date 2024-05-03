from django.utils import timezone
from .models import *
from random import (
    randint,
    uniform,
    choice
)
from faker import Faker

fake = Faker()


def create_vendor_and_po_objets():
    vendor_obj = Vendor.objects.create(
        name=fake.name(),
        contact_details=fake.phone_number(),
        address=fake.address(),
        vendor_code=fake.uuid4(),
        on_time_delivery_rate=randint(10, 100),
        quality_rating_avg=randint(1, 5),
        average_response_time=uniform(0.0001, 1000),
        fulfillment_rate=randint(10, 100),
    )
    po_object = PurchaseOrder.objects.create(
        po_number=fake.uuid4(),
        vendor=vendor_obj,
        order_date=fake.date_this_year(
            before_today=True, after_today=False),
        delivery_date=fake.date_this_year(
            after_today=True, before_today=False),
        items=fake.json(num_rows=10),
        quantity=randint(1, 20),
        status=choice(("COMPLETED", "PENDING", "CANCELLED")),
        quality_rating=randint(1, 5),
        issue_date=timezone.make_aware(
            fake.date_time_this_year(before_now=True, after_now=False)),
        acknowledgement_date=timezone.make_aware(
            fake.date_time_this_year(after_now=True, before_now=False)),
    )

    # return final instance of objects for reusability
    return vendor_obj, po_object
