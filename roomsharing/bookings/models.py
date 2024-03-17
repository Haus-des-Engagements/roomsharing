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
