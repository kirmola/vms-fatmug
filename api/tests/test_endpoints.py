from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import PurchaseOrder, Vendor
from faker import Faker
from random import (
    randint,
    uniform,
    choice
)
from django.contrib.auth.models import User
from django.utils import timezone
from api.logics import create_vendor_and_po_objets
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class PurchaseOrderTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = f"Token {self.token.key}")
        self.fake = Faker()

    def test_vendor_route(self):
        vendor_code = self.fake.uuid4()

        list_route = reverse("vendor-list")
        detail_route = reverse("vendor-detail", kwargs={
            "pk": vendor_code
        })

        data = {
            "vendor_code": vendor_code,
            "name": self.fake.name(),
            "contact_details": self.fake.phone_number(),
            "address": self.fake.address(),
            "on_time_delivery_rate": randint(10, 100),
            "quality_rating_avg": randint(1, 5),
            "average_response_time": uniform(0.0001, 1000),
            "fulfillment_rate": randint(10, 100)
        }


        #   Create vendor and assert creation
        response = self.client.post(list_route, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #   List vendors and assert itrs existance
        response = self.client.get(list_route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #   Retrieve vendor's assertion
        vendor_obj = Vendor.objects.filter(vendor_code=vendor_code).exists()
        self.assertEqual(vendor_obj, True)

        #   Update/patch vendor and assert update
        update_data = {
            "contact_details": "9999999999",
        }

        response = self.client.patch(detail_route, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #   Verify patched data
        updated_contact_detail = Vendor.objects.get(
            vendor_code=vendor_code).contact_details
        self.assertEqual(updated_contact_detail, "9999999999")

        #   Delete Vendor and assert deletion

        response = self.client.delete(detail_route)
        vendor_exists = Vendor.objects.filter(vendor_code=vendor_code).exists()
        self.assertEqual(vendor_exists, False)

    def test_purchase_order_routes(self):

        po_number = self.fake.uuid4()
        vendor_id = self.fake.uuid4()
        list_route = reverse('purchaseorder-list')
        detail_route = reverse("purchaseorder-detail", kwargs={
            "pk": po_number
        })

        vendor_obj = create_vendor_and_po_objets()[0]

        data = {
            "po_number": po_number,
            "vendor": vendor_obj.vendor_code,
            "order_date": self.fake.date_this_year(
                before_today=True, after_today=False),
            "delivery_date": self.fake.date_this_year(
                after_today=True, before_today=False),
            "items": self.fake.json(num_rows=5),
            "quantity": randint(1, 20),
            "status": choice(("COMPLETED", "PENDING", "CANCELLED")),
            "quality_rating": randint(1, 5),
            "issue_date": timezone.make_aware(
                self.fake.date_time_this_year(before_now=True, after_now=False)),
            "acknowledgement_date": timezone.make_aware(
                self.fake.date_time_this_year(after_now=True, before_now=False)),

        }


        #   Create PO's
        response = self.client.post(list_route, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.filter(po_number=po_number).get().po_number, po_number)

        #   List PO's

        response = self.client.get(list_route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #   Retrieve PO's assertion
        self.assertEqual(PurchaseOrder.objects.filter(
            po_number=po_number).exists(), True)

        #   Update/patch PO's and assert updates

        update_data = {
            "quantity": 3000
        }

        response = self.client.patch(detail_route, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #   Verify patched data
        updated_quantity = PurchaseOrder.objects.get(
            po_number=po_number).quantity
        self.assertEqual(updated_quantity, 3000)

        #   Delete PO's and assert deletion

        response = self.client.delete(detail_route)
        po_exists = PurchaseOrder.objects.filter(po_number=po_number).exists()
        self.assertEqual(po_exists, False)

    # def test_get_purchase_order(self):
    #     purchase_order = PurchaseOrder.objects.create(
    #         po_number='PO456',
    #         vendor_id=1,  # Assuming vendor ID 1 exists
    #         order_date='2022-02-01T00:00:00Z',
    #         delivery_date='2022-02-10T00:00:00Z',
    #         items={'item1':"details1', 'item2':"details2'},
    #         quantity=20,
    #         status='PENDING',
    #         quality_rating=3,
    #     )
    #     # Assuming 'purchaseorder-detail' is your detail endpoint URL
    #     url = reverse('purchaseorder-detail', kwargs={'pk': purchase_order.pk})
