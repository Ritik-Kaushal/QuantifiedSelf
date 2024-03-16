from django.db import models
from django.contrib.auth.models import User

class TrackerType(models.Model):
    name = models.CharField(max_length = 25, unique=True)

    def __str__(self) -> str:
        return self.name
    
class Tracker(models.Model):
    name = models.CharField(max_length = 25)
    description = models.TextField(default = '-')
    type = models.ForeignKey(TrackerType, to_field = 'name', on_delete = models.CASCADE)
    user = models.ForeignKey(User, to_field = 'id',on_delete = models.CASCADE)
    times_edited = models.IntegerField(default=0)
    last_edited = models.DateField()
    reqd_values = models.CharField(null=True,max_length = 50)

    def __str__(self) -> str:
        return f"{self.user.id}-{self.user.username}-{self.name}"

class TrackerLogs(models.Model):
    time_stamp = models.DateField()
    tracker = models.ForeignKey(Tracker, on_delete = models.CASCADE, related_name = 'logs')
    value = models.CharField(max_length = 128)
    note = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.tracker.user.id}-{self.tracker.name}-{self.time_stamp}"
