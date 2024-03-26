# Generated by Django 4.2.11 on 2024-03-26 09:16

from django.conf import settings
import django.contrib.postgres.constraints
import django.contrib.postgres.fields.ranges
from django.contrib.postgres.operations import BtreeGistExtension
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('users', '0002_organization_alter_user_options_remove_user_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        BtreeGistExtension(),
        migrations.CreateModel(
            name='BookingGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookinggroups_of_organization', related_query_name='bookinggroup_of_organization', to='users.organization', verbose_name='Booking Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookinggroups_of_user', related_query_name='bookinggroup_of_user', to=settings.AUTH_USER_MODEL, verbose_name='Initial Booking User')),
            ],
            options={
                'verbose_name': 'Booking Group',
                'verbose_name_plural': 'Booking Groups',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('timespan', django.contrib.postgres.fields.ranges.DateTimeRangeField(default_bounds='()', verbose_name='Date Time Range')),
                ('booking_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings_of_bookinggroup', related_query_name='booking_of_bookinggroup', to='bookings.bookinggroup', verbose_name='Booking Group')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings_of_room', related_query_name='booking_of_room', to='rooms.room', verbose_name='Room')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ['timespan'],
            },
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(expressions=[('timespan', '&&'), ('room', '=')], name='exclude_overlapping_reservations'),
        ),
    ]
