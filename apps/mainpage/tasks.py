import datetime

import requests
from celery import shared_task

from apps.mainpage.models import TelegramBot

bot_token = '5781542580:AAFQs7jLyx_Fioru3gYxo9YdtOx1sQwvNzc'
chat_id = '-1001704309348'


@shared_task
def date_kick():
    user_list = TelegramBot.objects.filter()
    data = ""
    for user in user_list:
        if user.and_date >= datetime.datetime.now():
            url = f"https://api.telegram.org/bot{bot_token}/kickChatMember?chat_id={chat_id}&user_id={user.user_id}"
            requests.post(url)
            data += user.username + ","
    return data
