# To use Celery with Django project, must define an instance of the Celery library (called “app”)

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerydjango.settings')


app = Celery('celerydjango')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# Running default Celery worker : $ celery -A celerydjango worker --loglevel=INFO --pool=solo  
# Running default worker on new defined queue : $ celery -A celerydjango worker -Q queue2
# Monitoring with Flower : $ celery -A celeryudango flower :  http://localhost:5555/dashboard

# To create and run two celery workers, use two commands :
# $ celery -A [PROJECT_APP] worker -n [WORKER_NAME] -Q default
# $ celery -A [PROJECT_APP] worker -n [WORKER_NAME] -Q queue2

# Two queues (default and queue2) + two workers (defaut + worker2) steps / each task in own queue/worker :
# 1 - Create and define queues in settings.py : app.conf.tasks_queues
# 2 - Running celery workers, two commands
# 3 - Route the tasks to the correct worker in settings.py : CELERY_TASK_ROUTES   