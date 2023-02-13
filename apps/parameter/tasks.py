from __future__ import absolute_import, unicode_literals

import datetime

import requests
from celery import shared_task


@shared_task()
def kick_user():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot_token = '5781542580:AAFQs7jLyx_Fioru3gYxo9YdtOx1sQwvNzc'
    chat_id = '-1001704309348'
    user_id = '1017850259'
    requests.post(f"https://api.telegram.org/bot{bot_token}/kickChatMember?chat_id={chat_id}&user_id={user_id}")
    print(f"Sistem Tarama Zamanı {current_time}")
