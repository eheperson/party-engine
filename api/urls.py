from django.urls import path
from django.urls.conf import include
from .views import main, CreateRoomView
from .views import RoomView

urlpatterns = [
    path('main', main, name='root'),
    path('room', RoomView.as_view(), name='Room View'),
    path('create-room', CreateRoomView.as_view(), name="Create Room"),
]
