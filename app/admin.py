from django.contrib import admin
from .models import TypeRoom, Room, Reservation

admin.site.register(TypeRoom)
admin.site.register(Room)
admin.site.register(Reservation)