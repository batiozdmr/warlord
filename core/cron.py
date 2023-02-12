import datetime

import requests
from django_q.tasks import async_task

from apps.mainpage.models import TelegramBot


def repeat_task():
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
    print("MyCronJob'u Çalıştırma")


async_task(repeat_task, repeat=60)  # Task every 60 seconds