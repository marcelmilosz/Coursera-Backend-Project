from django.shortcuts import render
from django.http import HttpResponse

# Api / Rest
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer, MenuItemSerializer


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
