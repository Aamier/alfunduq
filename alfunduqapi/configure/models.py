from django.db import models


class RoomType(models.Model):
    roomtype_id = models.AutoField(primary_key=True, default=None)
    rate = models.IntegerField()
    desc = models.TextField()
    type_name = models.CharField(max_length=100, default=None)


class Floor(models.Model):
    floor_number = models.IntegerField(primary_key=True, unique=True, default=None)
    floor_name = models.CharField(max_length=20)


class Rooms(models.Model):
    number = models.AutoField(primary_key=True, default=None)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
