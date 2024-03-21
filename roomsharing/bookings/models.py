from datetime import datetime
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
    timespan = DateTimeRangeField("Date Time Range", default_bounds="[]")
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


def generate_free_slots(bookings):
    free_slots_by_room = {}
    previous_end_time = {}

    for booking in bookings:
        room_id = booking.room_id
        start_time = booking.timespan.lower
        end_time = booking.timespan.upper

        if room_id not in free_slots_by_room:
            free_slots_by_room[room_id] = []
            previous_end_time[room_id] = None

        if previous_end_time[room_id] and start_time > previous_end_time[room_id]:
            # Prüfe auf Übernacht-Slots und teile slot auf
            if previous_end_time[room_id].date() != start_time.date():
                # Erstellt einen Slot bis 23:59 am Startdatum
                end_of_start_day = datetime.combine(
                    previous_end_time[room_id].date(),
                    datetime.max.time().replace(second=0, microsecond=0),
                )
                free_slots_by_room[room_id].append(
                    (previous_end_time[room_id], end_of_start_day)
                )

                # Erstellt einen Slot ab 00:00 Uhr am Enddatum
                start_of_end_day = datetime.combine(
                    start_time.date(), datetime.min.time()
                )
                free_slots_by_room[room_id].append((start_of_end_day, start_time))

                previous_end_time[room_id] = end_time
            else:
                # normaler slot:
                free_slots_by_room[room_id].append(
                    (previous_end_time[room_id], start_time)
                )
                previous_end_time[room_id] = end_time
        else:
            previous_end_time[room_id] = end_time

    return free_slots_by_room


def prettyprint_slots(free_slots):
    from colorama import Fore
    from colorama import Style

    current_date = None
    for room, slots in free_slots.items():
        print(Fore.GREEN + f"Raum {Rooms.objects.get(id=room).name}:")
        for start, end in slots:
            if start.strftime("%m-%d") != current_date:
                current_date = start.strftime("%m-%d")
                year = start.strftime("%Y")
                print(
                    f"\n  {Fore.YELLOW}{current_date}{Fore.LIGHTBLACK_EX}-{year}:{Style.RESET_ALL}",
                    end=" ",
                )
            print(
                f"{Fore.CYAN}⏰ {start.strftime('%H:%M')}-{end.strftime('%H:%M')}",
                end=" ",
            )
        current_date = None  # Reset for the next room
        print("\n")  # Better separation between rooms
