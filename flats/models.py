from django.db import models

class Flats(models.Model):
    object_name = models.CharField(max_length=200)
    floor = models.IntegerField()
    rooms_count = models.IntegerField()
    total_square = models.FloatField()
    price = models.FloatField()

class ObjectsHistory(models.Model):
    object_name = models.CharField(max_length=200)
    flats_count = models.IntegerField()
    date = models.DateField()

class Buildings(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class FlatsNumber(models.Model):
    building = models.ForeignKey(Buildings)
    one_room = models.IntegerField()
    two_rooms = models.IntegerField()
    three_rooms = models.IntegerField()
    four_or_more_rooms = models.IntegerField()
    date = models.DateField()

    def __unicode__(self):
        return '%s | %s | %s | %s | %s | %s' % (self.building.name, self.one_room,
                                                self.two_rooms, self.three_rooms,
                                                self.four_or_more_rooms, self.date)
