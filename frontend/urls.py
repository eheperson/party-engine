from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('join', index, name='join to room'),
    path('create', index, name='create a room'),
    path('join/1', index, name='join to room with num'),
]