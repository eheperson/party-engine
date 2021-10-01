from django.urls import path
from django.urls.conf import include
from .views import main, CreateRoomView
from .views import RoomView, GetRoom, JoinRoom

urlpatterns = [
    path('main', main, name='root'),
    path('room', RoomView.as_view(), name='Room View'),
    path('create-room', CreateRoomView.as_view(), name="Create Room"),
    path('get-room', GetRoom.as_view(), name="Get Room"), # http://127.0.0.1:8000/api/get-room?code=LEENAC
    path('join-room', JoinRoom.as_view())
]
