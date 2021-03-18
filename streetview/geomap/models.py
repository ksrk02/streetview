from django.db import models

class TileMap(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField('zoom level')
