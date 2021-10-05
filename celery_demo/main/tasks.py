from celery_demo.celery import app

@app.task(bind=True)
def value_of_pi(self):
    print('Request: {0!r}'.format(self.request))