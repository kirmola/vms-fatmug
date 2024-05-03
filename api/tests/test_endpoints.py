from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import PurchaseOrder, Vendor
from faker import Faker
from random import randint, uniform
from django.contrib.auth.models import User


class PurchaseOrderTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username="testuser", password="testpassword")
        self.fake = Faker()

    def test_vendor_route(self):
        vendor_code = self.fake.uuid4()

        list_route = reverse("vendor-list")
        detail_route = reverse("vendor-detail", kwargs={
            "pk": vendor_code
        })

        #   Create vendor

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

        #   Login user forcefully for testing
        self.client.force_login(user=self.user)

        #   Create vendor and assert creation
        response = self.client.post(list_route, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #   List vendors and assert itrs existance
        response = self.client.get(list_route)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        vendor_obj = Vendor.objects.get(vendor_code=vendor_code).vendor_code
        self.assertEqual(vendor_obj, vendor_code)

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

    # def test_vendor_detail_route(self):
    #     url = reverse("vendor-detail")
    #     primary_key =
    #     self.client.force_login(user=self.user)

        #   Retrieve Vendor Detail

        #   Update Vendor Detail

        #   Delete Vendor Detail

        # data = {
        #     "vendor_code": self.vendor_code
        # }
        # response = self.client.delete(url, data=data)

        # print(response.status_code)

    # def test_create_purchase_order(self):
    #     url = reverse('purchaseorder-list')
    #     data = {
    #         'po_number': 'PO123',
    #         'vendor': 1
    #         'order_date': '2022-01-01T00:00:00Z',
    #         'delivery_date': '2022-01-10T00:00:00Z',
    #         'items': {'item1': 'details1', 'item2': 'details2'},
    #         'quantity': 10,
    #         'status': 'COMPLETED',
    #         'quality_rating': 5,
    #     }

    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(PurchaseOrder.objects.count(), 1)
    #     self.assertEqual(PurchaseOrder.objects.get().po_number, 'PO123')

    # def test_get_purchase_order(self):
    #     purchase_order = PurchaseOrder.objects.create(
    #         po_number='PO456',
    #         vendor_id=1,  # Assuming vendor ID 1 exists
    #         order_date='2022-02-01T00:00:00Z',
    #         delivery_date='2022-02-10T00:00:00Z',
    #         items={'item1': 'details1', 'item2': 'details2'},
    #         quantity=20,
    #         status='PENDING',
    #         quality_rating=3,
    #     )
    #     # Assuming 'purchaseorder-detail' is your detail endpoint URL
    #     url = reverse('purchaseorder-detail', kwargs={'pk': purchase_order.pk})
