from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True)


class Reminder(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    body = models.CharField(max_length=500, blank=True)
    scheduled_at = models.DateTimeField()
