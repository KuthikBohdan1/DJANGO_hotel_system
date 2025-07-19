from django.shortcuts import render, get_object_or_404, redirect
from .models import Room
from app.form import BookingForm
from django.contrib.auth.decorators import login_required

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


@login_required 
def booking(request, id_room):
    room = Room.objects.get(id = id_room)
    form = BookingForm()
    if request.method == "POST":
        if form.is_valid():
            reservation =  form.save(commit=False)
            reservation.room = room 
            reservation.reservator = request.user
            reservation.save()
            return redirect("room_list")

    
    
    context = {
        'room' : room,
        'form' : form ,
    }
    return render(
        request,
        template_name="booking.html",
        context=context,

    )