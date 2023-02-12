import os

from celery import Celery

app = Celery('tasks', broker=os.environ['REDIS_URL'])


@app.task
def add(x, y):
    print(x + y)
    return x + y
