from django.db import models

class Flats(models.Model):
    object_name = models.CharField(max_length=200)
    floor = models.IntegerField()
    rooms_count = models.IntegerField()
    total_square = models.FloatField()
    price = models.FloatField()

class ObjectsHistory(models.Model):
    object_name = models.CharField(max_length=200)
    one_room_count = models.IntegerField()
    two_room_count = models.IntegerField()
    three_room_count = models.IntegerField()
    four_or_more_room_count = models.IntegerField()
    date = models.DateField()

    def __unicode__(self):
        return self.object_name
