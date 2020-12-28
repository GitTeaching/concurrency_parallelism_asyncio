from celery import Celery
import time


# Celery instance / Celery application or just app for short
# This instance is used as the entry-point for everything you want to do in Celery
# The first argument to Celery is the name of the current module
# The second argument is specifying the URL of the message broker (ex RabbitMQ)
# To keep track of the tasks’ states, Celery needs to store or send the states somewhere (rpc, db, etc.)
app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


# Celery task
@app.task
def add(x, y):
	time.sleep(10)
	return x + y


# Running Celery worker server : $ celery -A tasks worker --loglevel=INFO --pool=solo  /or -P threads
