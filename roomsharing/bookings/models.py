from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Bookings(models.Model):
    date = models.DateField()
    start_time = models.DateTimeField("Start time")
    end_time = models.DateTimeField("End time")
    room = models.ForeignKey(
        Rooms,
        on_delete=models.PROTECT,
        related_name="bookings_of_room",
        related_query_name="booking_of_room",
    )

    def __str__(self):
        return self.id
