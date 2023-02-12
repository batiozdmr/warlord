from __future__ import absolute_import, unicode_literals

import requests
from celery import shared_task


@shared_task(name="data_checking")
def data_add():
    bot_token = '5781542580:AAFQs7jLyx_Fioru3gYxo9YdtOx1sQwvNzc'
    chat_id = '-1001704309348'
    user_id = '1017850259'
    requests.post(f"https://api.telegram.org/bot{bot_token}/kickChatMember?chat_id={chat_id}&user_id={user_id}")
    return 'test'
