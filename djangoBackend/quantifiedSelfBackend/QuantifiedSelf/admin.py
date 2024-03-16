from django.contrib import admin
from QuantifiedSelf import models

# Register your models here.
admin.site.register(models.TrackerType)
admin.site.register(models.Tracker)
admin.site.register(models.TrackerLogs)
