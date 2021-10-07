from django.db import models


class Reminder(models.Model):
    heading = models.CharField(max_length=50)
    body = models.CharField(max_length=500, blank=True)
    scheduled_at = models.DateTimeField()
