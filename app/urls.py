from django.urls import path
from app import views 

urlpatterns = [
    path('list/', views.room_list, name='room_list'),
    path('booking/<int:id_room>', views.booking, name='booking'),
]