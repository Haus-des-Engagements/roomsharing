# Generated by Django 4.2.11 on 2024-03-21 21:24

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookings",
            name="timespan",
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(
                default_bounds="[]", verbose_name="Date Time Range"
            ),
        ),
    ]
