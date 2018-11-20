from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from configure import models, serializers
import json


class Floor(APIView):
    """
    List all rooms, or create a new room.
    """

    def get(self, request, format=None):
        floor_obj = models.Floor.objects.all()
        floor_serializer = serializers.FloorSerializer(floor_obj, many=True)
        serializer = floor_serializer.data
        return Response(serializer)

    def post(self, request, format=None):
        json_payload = json.loads(str(request.body, encoding='utf-8'))
        serializer = serializers.FloorSerializer(data=json_payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomType(APIView):
    """
    List all rooms, or create a new room.
    """

    def get(self, request, format=None):
        room_type_obj = models.RoomType.objects.all()
        room_type_serializer = serializers.RoomTypeSerializer(room_type_obj, many=True)
        serializer = room_type_serializer.data
        return Response(serializer)

    def post(self, request, format=None):
        json_payload = json.loads(str(request.body, encoding='utf-8'))
        serializer = serializers.RoomTypeSerializer(data=json_payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomsList(APIView):
    """
    List all rooms, or create a new room.
    """

    def get(self, request, format=None):
        rooms_obj = models.Room.objects.all()
        rooms_serializer = serializers.RoomSerializer(rooms_obj, many=True)
        serializer = rooms_serializer.data
        return Response(serializer)

    def post(self, request, format=None):
        json_payload = json.loads(str(request.body, encoding='utf-8'))
        print(json_payload)
        serializer = serializers.RoomCreateSerializer(data=json_payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacilityList(APIView):
    """
    List all rooms, or create a new room.
    """

    def get(self, request, format=None):
        facility_obj = models.Facility.objects.all()
        facility_serializer = serializers.FacilitySerializer(facility_obj, many=True)
        serializer = facility_serializer.data
        return Response(serializer)

    def post(self, request, format=None):
        json_payload = json.loads(str(request.body, encoding='utf-8'))
        print(json_payload)
        serializer = serializers.FacilitySerializer(data=json_payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)