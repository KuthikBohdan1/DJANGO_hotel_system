from django.shortcuts import render, get_object_or_404
from .models import Room

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()

    context = {
        "all_text": "text",
        "rooms": rooms,
    }
    return render(
        request,
        template_name="room_list.html",
        context=context,
    )

def booking(request, id_room):
    room = Room.objects.get(id = id_room)
    context = {
        'room' : room
    }
    return render(
        request,
        template_name="booking.html",
        context=context,

    )