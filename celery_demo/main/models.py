from django.db import models


class Reminder(models.Model):
    heading = models.CharField(max_length=50)
    body = models.TextField()
    scheduled_at = models.DateTimeField()
