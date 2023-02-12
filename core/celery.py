from __future__ import absolute_import, unicode_literals

import os

import requests
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    bot_token = '5781542580:AAFQs7jLyx_Fioru3gYxo9YdtOx1sQwvNzc'
    chat_id = '-1001704309348'
    user_id = '1017850259'
    requests.post(f"https://api.telegram.org/bot{bot_token}/kickChatMember?chat_id={chat_id}&user_id={user_id}")
    print('Request: {0!r}'.format(self.request))
    print('hello world')


app.conf.beat_schedule = {
    'add-every-minute-contrab': {
        'task': 'data_checking',
        'schedule': crontab(minute=1),
    },
}
