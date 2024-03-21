import csv

from roomsharing.bookings.models import Bookings
from roomsharing.bookings.models import Rooms

with open("poc_bookings_teamup_0_0_5.csv") as file:
    reader = csv.DictReader(file, delimiter=";")
    for i, row in enumerate(reader):
        if i >= 10000:
            break  # Stoppt nach den ersten 10 Zeilen
        # print(row)
        # Suche nach dem Raum über die ID
        try:
            room = Rooms.objects.get(id=int(row["room_id"]))
        except:
            print(f"Raum mit ID {row['room_id']} nicht gefunden. Überspringe Eintrag.")
            continue  # Geht zum nächsten Eintrag über, ohne diesen zu verarbeiten

        item = Bookings(
            timespan=row["timespan"],
            room=room,
        )
        try:
            item.save()
        except Exception as err:
            print(f"failed to import booking with ID {row['id']} {err}")
