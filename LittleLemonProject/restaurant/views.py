from django.shortcuts import render
from django.http import HttpResponse

# Api / Rest
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import (
    MenuSerializer,
    MenuItemSerializer,
    BookingSerializer,
    BookingItemSerializer,
)


# Create your views here.


def index(request):
    return render(request, "index.html", {})


def home(request):
    return HttpResponse("Home")


class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()  # Retrieve all objects
    serializer_class = MenuItemSerializer


class BookingView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class SingleBookingItemView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()  # Retrieve all objects
    serializer_class = BookingItemSerializer
