# Generated by Django 5.0.4 on 2024-05-01 06:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(max_length=75, verbose_name="Vendor's Name")),
                ('contact_details', models.TextField(verbose_name="Vendor's Contact Information")),
                ('address', models.TextField(verbose_name="Vendor's Physical Address")),
                ('vendor_code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name="Vendor's Unique Identifier")),
                ('on_time_delivery_rate', models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=100)], verbose_name='Percentage of On-time delivery')),
                ('quality_rating_avg', models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=5)], verbose_name='Quality Rating')),
                ('average_response_time', models.FloatField(verbose_name='Average Response time of vendor')),
                ('fulfillment_rate', models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=100)], verbose_name='Order Fulfillment rate of vendor')),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_number', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Unique PO Number')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Order Date')),
                ('delivery_date', models.DateTimeField(auto_now=True, verbose_name='Delivery Date')),
                ('items', models.JSONField(default=dict, verbose_name='Ordered Items Details')),
                ('quantity', models.IntegerField(verbose_name='Quantity of Items')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], max_length=50, verbose_name='Order Status')),
                ('quality_rating', models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=5)], verbose_name='Quality Rating of Order')),
                ('issue_date', models.DateTimeField(default=None, verbose_name='Order Issue Date to the Vendor')),
                ('acknowledgement_date', models.DateTimeField(default=None, verbose_name='Order Acknowledgment Date')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor', verbose_name='Vendor')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Orders',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, unique=True, verbose_name='Date of Performace Record')),
                ('on_time_delivery_rate', models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=100)], verbose_name='Percentage of On-time delivery')),
                ('avg_response_time', models.FloatField(default=None, verbose_name='Average Response time')),
                ('quality_rating_avg', models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=5)], verbose_name='Average Quality Rating')),
                ('fulfillment_rate', models.FloatField(default=None, validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=100)], verbose_name='Order Fulfillment rate of vendor')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vendor', verbose_name='Vendor')),
            ],
            options={
                'verbose_name': 'Performance',
                'verbose_name_plural': 'Performance Detail',
            },
        ),
    ]
