from django.test import TestCase
from faker import Faker
from faker.providers import company
from api.models import PurchaseOrder, Vendor
from random import choice, randint, uniform
from django.utils import timezone
from api.logics import create_vendor_and_po_objets


class ModelTesting(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(company)
        self.test_times = 10  # Change accordingly

    def test_create_purchase_orders_with_fake_data(self):
        for _ in range(self.test_times):
            objs = create_vendor_and_po_objets()
            vendor_obj, po_object = objs[0], objs[1]
            self.assertGreaterEqual(
                po_object.acknowledgement_date, po_object.order_date)
            self.assertGreaterEqual(
                po_object.acknowledgement_date, po_object.issue_date)
