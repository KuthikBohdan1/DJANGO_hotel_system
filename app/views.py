from django.shortcuts import render
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