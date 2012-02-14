from django.db import models

# Create your models here.
class Building(models.Model):
    Number = models.CharField(max_length=60)
    Description = models.CharField(max_length=120)
    OSMURL = models.CharField(max_length=300) # an url, i dont know if they have different types
    Lat = models.CharField(max_length=20)  #lat/lon of then center
    Lon = models.CharField(max_length=20) # lat/lon of the center of the building


class BuildingPoint(models.Model):
    parent      = models.ForeignKey('Building', null=False, blank=False, related_name='points')
    OSMNODEID = models.DecimalField(decimal_places=0, max_digits=15) # the osm id
    Lat = models.CharField(max_length=20)  #lat/lon of then center
    Lon = models.CharField(max_length=20) # lat/lon of the center of the building
