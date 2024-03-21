import csv

from roomsharing.bookings.models import Rooms

with open("rooms.csv") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        item = Rooms(name=row[1])
        item.save()
