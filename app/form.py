from django import forms
from django.forms import Reservation

class BookingForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['date_start', 'date_end', 'phone']