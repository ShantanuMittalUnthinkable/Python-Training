from celery import shared_task
from kafka import KafkaProducer


@shared_task
def set_reminder(reminder):
    """
    Celery task to push reminder data to SMS API

    #Args:
    reminder - Reminder model object
    """
    producer = KafkaProducer()
