from ogp_import.models import Building
from ogp_import.models import BuildingPoint
from ogp_import.models import Facinet
from ogp_import.models import Logger
from ogp_import.models import LoggerMeasurement

from django.contrib import admin

admin.site.register(Building)
admin.site.register(BuildingPoint)
admin.site.register(Facinet)
admin.site.register(Logger)
admin.site.register(LoggerMeasurement)
