from django.db import models


class RoomType(models.Model):
    type_id = models.CharField(max_length=10)
    rate = models.IntegerField()
    desc = models.TextField()
    type_name = models.CharField(max_length=100, default=None)


class Floor(models.Model):
    floor_id = models.AutoField(primary_key=True, default=None)
    floor_number = models.IntegerField(default=None)
    floor_name = models.CharField(max_length=20)


class Rooms(models.Model):
    number = models.AutoField(primary_key=True, default=None)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
