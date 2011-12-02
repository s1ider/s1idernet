from django.db import models

class Flats(models.Model):
    object_name = models.CharField(max_length=200)
    floor = models.IntegerField
    rooms_count = models.IntegerField
    total_square = models.FloatField
    price = models.FloatField


