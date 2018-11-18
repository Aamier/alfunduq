# rooms/urls.py
from django.urls import path
from django.conf.urls import url
from . import views
from . import create_hotel_base

urlpatterns = [
    path('rooms', create_hotel_base.RoomsList.as_view()),
    path('floors', create_hotel_base.Floor.as_view()),
    path('roomtype', create_hotel_base.RoomType.as_view()),
    url(r'^(?P<pk>[0-9]+)/floor/$', views.Floor.as_view()),
]