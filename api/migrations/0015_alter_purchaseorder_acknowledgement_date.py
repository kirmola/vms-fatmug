# Generated by Django 5.0.4 on 2024-05-02 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_purchaseorder_acknowledgement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgement_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 2, 16, 50, 50, 790902), verbose_name='Order Acknowledgment Date'),
        ),
    ]
