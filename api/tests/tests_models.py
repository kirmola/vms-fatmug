from django.test import TestCase
from faker import Faker
from faker.providers import company
from ..models import PurchaseOrder, Vendor
from random import choice, randint, uniform
from django.utils import timezone


class ModelTesting(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(company)
        self.test_times = 10  # Change accordingly

    def test_create_purchase_orders_with_fake_data(self):
        for _ in range(self.test_times):
            vendor_obj = Vendor.objects.create(
                name=self.fake.name(),
                contact_details=self.fake.phone_number(),
                address=self.fake.address(),
                vendor_code=self.fake.uuid4(),
                on_time_delivery_rate=randint(10, 100),
                quality_rating_avg=randint(1, 5),
                average_response_time=uniform(0.0001, 1000),
                fulfillment_rate=randint(10, 100),
            )

            po_object = PurchaseOrder.objects.create(
                po_number=self.fake.uuid4(),
                vendor=vendor_obj,
                order_date=self.fake.date_this_year(
                    before_today=True, after_today=False),
                delivery_date=self.fake.date_this_year(
                    after_today=True, before_today=False),
                items=self.fake.json(num_rows=10),
                quantity=randint(1, 20),
                status=choice(("COMPLETED", "PENDING", "CANCELLED")),
                quality_rating=randint(1, 5),
                issue_date=timezone.make_aware(
                    self.fake.date_time_this_year(before_now=True, after_now=False)),
                acknowledgement_date=timezone.make_aware(
                    self.fake.date_time_this_year(after_now=True, before_now=False)),
            )

            self.assertGreaterEqual(
                po_object.acknowledgement_date, po_object.order_date)
            self.assertGreaterEqual(
                po_object.acknowledgement_date, po_object.issue_date)
