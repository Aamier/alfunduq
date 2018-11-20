
from rest_framework import serializers
from configure import models


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Facility
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomType
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Floor
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    floor = FloorSerializer(many=False, read_only=True)
    room_type = RoomTypeSerializer(many=False, read_only=True)

    class Meta:
        model = models.Room
        fields = '__all__'
        # fields = ('room_no', 'floor', 'room_type')


class RoomCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = '__all__'
