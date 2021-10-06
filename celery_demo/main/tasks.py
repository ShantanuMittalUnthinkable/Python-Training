from celery import shared_task

@shared_task
def value_of_pi():
    counter = 0
    print(counter)
    counter += 1
    return counter