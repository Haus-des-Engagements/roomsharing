from datetime import timedelta

from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import DateTimeRangeField
from django.contrib.postgres.fields import RangeOperators
from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Bookings(models.Model):
    timespan = DateTimeRangeField("Date Time Range", default_bounds="()")
    room = models.ForeignKey(
        Rooms,
        on_delete=models.PROTECT,
        related_name="bookings_of_room",
        related_query_name="booking_of_room",
    )

    class Meta:
        constraints = [
            ExclusionConstraint(
                name="exclude_overlapping_reservations",
                expressions=[
                    ("timespan", RangeOperators.OVERLAPS),
                    ("room", RangeOperators.EQUAL),
                ],
            ),
        ]

    def __str__(self):
        return str(self.id)


def find_available_rooms(start_times, duration):
    available_rooms_by_slot = {}
    slot_duration = timedelta(hours=duration)

    for start_time in start_times:
        end_time = start_time + slot_duration

        # Query bookings that overlap with the time slot
        overlapping_bookings = Bookings.objects.filter(
            timespan__overlap=(start_time, end_time),
        )

        # Get the list of booked room IDs
        booked_room_ids = overlapping_bookings.values_list("room_id", flat=True)

        # Query rooms that are not booked during the time slot
        available_rooms = Rooms.objects.exclude(id__in=booked_room_ids)
        available_rooms_by_slot[start_time] = available_rooms

    return available_rooms_by_slot
