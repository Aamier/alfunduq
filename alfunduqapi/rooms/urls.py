# rooms/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('rooms', views.RoomsList.as_view()),
    path('floors', views.Floor.as_view()),
    path('roomtype', views.RoomType.as_view())
]