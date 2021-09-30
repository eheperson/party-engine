from django.urls import path
from django.urls.conf import include
from .views import main
from .views import RoomView

urlpatterns = [
    path('main', main, name='root'),
    path('room', RoomView.as_view(), name='Room View'),
]
