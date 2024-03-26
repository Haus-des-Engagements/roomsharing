from django.contrib import admin

from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ["id", "name", "square_meters", "max_persons"]
    search_fields = ["id", "name"]
    ordering = ["id"]
