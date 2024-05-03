from django.test import TestCase
from faker import Faker
from faker.providers import company
from ..models import PurchaseOrder, Vendor
from uuid import uuid4
from random import choice, randint, uniform
from django.utils import timezone

class ModelTesting(TestCase):

    def setUp(self):
        self.fake_company = Faker()
        self.fake_company.add_provider(company)

    def test_create_vendors_with_fake_data(self):
        vendor_obj = Vendor.objects.create(
            name=self.fake_company.company(),
            contact_details = self.fake_company.phone_number(),
            address = self.fake_company.address(),
            vendor_code = uuid4(),
            on_time_delivery_rate = randint(10,100),
            quality_rating_avg = randint(1, 5),
            average_response_time = uniform(0.0001, 1000),
            fulfillment_rate = randint(10,100),
        )
        return vendor_obj


    def test_create_purchase_orders_with_fake_data(self):
        vendor_obj = self.test_create_vendors_with_fake_data()
        po_object = PurchaseOrder.objects.create(
            po_number = uuid4(),
            vendor = vendor_obj,
            order_date = self.fake_company.date_this_year(before_today=True, after_today=False),
            delivery_date = self.fake_company.date_this_year(after_today=True, before_today=False),
            items = self.fake_company.json(num_rows=10),
            quantity = randint(1, 20),
            status = choice(("COMPLETED", "PENDING", "CANCELLED")),
            quality_rating = randint(1, 5),
            issue_date = timezone.make_aware(self.fake_company.date_time_this_year(before_now=True, after_now=False)) ,
            acknowledgement_date = timezone.make_aware(self.fake_company.date_time_this_year(after_now=True, before_now=False)),
        )

        self.assertGreaterEqual(po_object.acknowledgement_date, po_object.order_date) # type: ignore
        self.assertGreaterEqual(po_object.acknowledgement_date, po_object.issue_date) # type: ignore

        return po_object