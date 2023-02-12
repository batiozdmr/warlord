import json
import os

import requests
from django.shortcuts import render

bot_token = '5781542580:AAFQs7jLyx_Fioru3gYxo9YdtOx1sQwvNzc'
chat_id = '-1001704309348'


def send_message_to_telegram_group(message):
    send_message_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'

    response = requests.get(send_message_url)
    if response.status_code == 200:
        print("Message sent successfully.")
        print(response.text)
    else:
        print("Failed to send message.")
        print(response.text)


def get_user_count():
    # Kullanıcıları listelemek için API çağrısı
    response = f"https://api.telegram.org/bot{bot_token}/getChatMembersCount?chat_id={chat_id}"
    response = requests.get(response)
    # API cevabını JSON formatında parse et
    data = json.loads(response.text)

    # Kullanıcı sayısını yazdır
    print("Kullanıcı sayısı:", data)
    return data


def kick_user(user_id):
    url = f"https://api.telegram.org/bot{bot_token}/kickChatMember?chat_id={chat_id}&user_id={user_id}"
    response = requests.post(url)
    print(response.json())
    return response.json()


def index(request):
    data = os.environ.get('REDIS_URL', 'redis://localhost:6379')
    context = {
        'data': data
    }
    return render(request, "index.html", context)


def wrong403(request):
    return render(request, "404.html")


def wrong404(request):
    return render(request, "404.html")


def wrong500(request):
    return render(request, "404.html")
