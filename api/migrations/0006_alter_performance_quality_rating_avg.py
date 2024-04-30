# Generated by Django 5.0.4 on 2024-04-30 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_performance_quality_rating_avg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='quality_rating_avg',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=1), django.core.validators.MaxValueValidator(limit_value=5)], verbose_name='Average Quality Rating'),
        ),
    ]
