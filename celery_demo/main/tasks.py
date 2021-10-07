import json
from celery import shared_task
from kafka import KafkaProducer

from main.models import Reminder


@shared_task
def set_reminder(reminder):
    """
    Celery task to push reminder data to SMS API

    #Args:
    reminder - Reminder model object
    """
    rem = Reminder.objects.get(pk=reminder)
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda m: json.dumps(m).encode("ascii"),
    )
    producer.send(
        "email",
        {
            "heading": rem.heading,
            "body": rem.body,
            "scheduled_at": str(rem.scheduled_at),
        },
    )
