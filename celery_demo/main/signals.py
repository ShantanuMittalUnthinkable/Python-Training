import json
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .models import Reminder


# @receiver(post_save, sender=Reminder, dispatch_uid="update_stock_count")
# def update_stock(sender, instance, created, **kwargs):
#     print("RUNNING")
#     if created:
#         instance.product.stock -= instance.amount
#         instance.product.save()


@receiver(post_save, sender=Reminder)
def set_task(sender, instance, created, **kwargs):
    scheduled_datetime = instance.scheduled_at - timedelta(hours=5, minutes=30)
    if created:
        try:
            schedule = CrontabSchedule.objects.create(
                minute=scheduled_datetime.minute, hour=scheduled_datetime.hour
            )
            PeriodicTask.objects.create(
                name=instance.heading,
                task="main.tasks.set_reminder",
                crontab=schedule,
                expire_seconds=1,
                one_off=True,
                start_time=scheduled_datetime,
                args=json.dumps([str(instance.pk)]),
            )
        except:
            instance.delete()
