# Generated by Django 5.0.4 on 2024-05-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_purchaseorder_acknowledgement_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='acknowledgement_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Order Acknowledgment Date'),
        ),
    ]
