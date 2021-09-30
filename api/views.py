from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
# Create your views here.

def main(request):
    pass
    return HttpResponse("<h1> enivicivokki </h1>")

class RoomView(generics.CreateAPIView):
    """
        try : 'generics.ListAPIView' for only listing purpose
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer