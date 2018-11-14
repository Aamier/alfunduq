
from rest_framework import serializers
from rooms import models


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomType
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Floor
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    #floor = FloorSerializer(many=False, read_only=True)
    #room_type = RoomTypeSerializer(many=False, read_only=True)

    class Meta:
        model = models.Rooms
        fields = '__all__'
