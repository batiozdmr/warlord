web: gunicorn core.wsgi --log-file -
worker: celery -A apps.mainpage.tasks worker -l info