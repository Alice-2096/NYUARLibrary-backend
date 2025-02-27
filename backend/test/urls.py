"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('checkRoomAvailability/<slug:roomId>/', views.checkRoomAvailability),
    path('createRoom/', views.create_room),
    path('createLibrary/', views.create_library),
    path('createStudent/', views.create_student),
    path('getAllRooms/', views.get_all_rooms),
    path('getAllReservations/', views.get_all_reservations),
    path('getAllReservations/active/', views.get_all_reservations),
    path('createReservation/', views.create_reservation),
    path('adminUpdateBuffer/', views.adminUpdateBuffer),
    path('clearAllTimeSlots/', views.clearAllTimeSlots),
      path('reservations/', views.get_all_reservations_for_a_student),
]
