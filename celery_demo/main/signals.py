from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .models import Reminder


@receiver(post_save, sender=Reminder)
def set_task(sender, instance, **kwargs):

    scheduled_datetime = instance.scheduled_at

    # schedule = CrontabSchedule.objects.create(
    #     minute=scheduled_datetime.minute,
    #     hour=scheduled_datetime.hour
    # )
    print("Signal called")

    PeriodicTask.objects.create(
        name=instance.title,
        task="main.set_reminder",
        expire_seconds=1,
        one_off=True,
        start_time=scheduled_datetime,
    )
