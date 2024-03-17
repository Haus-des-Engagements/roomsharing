from django.contrib import admin  # Register your models here.

from .models import Bookings
from .models import Rooms


@admin.register(Rooms)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    pass
