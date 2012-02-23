from django.db import models


class Building(models.Model):
    Number = models.CharField(max_length=60)
    Description = models.CharField(max_length=120)
    OSMWAYID = models.DecimalField(decimal_places=0, max_digits=15) # the osm way id
    Lat = models.CharField(max_length=20)  #lat/lon of then center
    Lon = models.CharField(max_length=20) # lat/lon of the center of the building


class BuildingPoint(models.Model):
    parent      = models.ForeignKey('Building', null=False, blank=False, related_name='points')
    OSMNODEID = models.DecimalField(decimal_places=0, max_digits=15) # the osm id
    Lat = models.CharField(max_length=20)  #lat/lon of then center
    Lon = models.CharField(max_length=20) # lat/lon of the center of the building


class Facinet(models.Model):
    ##
    Building      = models.ForeignKey('Building', null=False, blank=False, related_name='FacinetNodes')
    location = models.IntegerField(unique=True, db_column='Location') # 
    name = models.TextField(db_column='Name') # 
    connectionstring = models.TextField(db_column='ConnectionString') # 
    tapidevice = models.TextField(db_column='TapiDevice', blank=True) # 
    synctime = models.CharField(max_length=3, db_column='SyncTime') # 
    online = models.CharField(max_length=3, db_column='Online') # 
    onlineall = models.CharField(max_length=3, db_column='OnlineAll') #    
    ## location for display
    Lat = models.CharField(max_length=20)  #lat/lon of facinet collector
    Lon = models.CharField(max_length=20) # lat/lon of facinet collector


class Logger(models.Model):
    Facinet      = models.ForeignKey('Facinet', null=False, blank=False, related_name='Loggers')
    loggerindex = models.IntegerField(unique=True, db_column='LoggerIndex') # 
    name = models.TextField(db_column='Name') # 
    online = models.IntegerField(db_column='Online') # 
   ## location for display
    Lat = models.CharField(max_length=20)  #lat/lon of the logger
    Lon = models.CharField(max_length=20) # lat/lon of the logger

class LoggerMeasurement(models.Model):
    Logger      = models.ForeignKey('Logger', null=False, blank=False, related_name='Measurement')
    timestamp   = models.DateTimeField()
    measurement = models.DecimalField(max_digits=12, decimal_places=4)
