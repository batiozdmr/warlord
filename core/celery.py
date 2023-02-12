from __future__ import absolute_import, unicode_literals

import datetime
import os

import requests
from celery import Celery
from django.conf import settings

from apps.mainpage.models import TelegramBot

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('channels_celery_heroku_project')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Istanbul')
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True)
def date_kick():
    bot_token = '5781542580:AAFQs7jLyx_Fioru3gYxo9YdtOx1sQwvNzc'
    chat_id = '-1001704309348'
    user_list = TelegramBot.objects.filter()
    data = ""
    for user in user_list:
        now_time = datetime.datetime.strptime(str(datetime.datetime.now()), "%Y-%m-%d %H:%M:%S.%f").strftime(
            "%Y-%m-%d %H:%M:%S+00:00")
        and_date = datetime.datetime.strptime(str(user.and_date), "%Y-%m-%d %H:%M:%S+00:00").strftime(
            "%Y-%m-%d %H:%M:%S+00:00")
        if now_time >= and_date:
            url = f"https://api.telegram.org/bot{bot_token}/kickChatMember?chat_id={chat_id}&user_id={user.user_id}"
            requests.post(url)
            data += user.username + ","
        user.delete()
    print(data)
    return data
