release: python manage.py migrate
web: gunicorn core.wsgi --log-file -
celery: celery -A core.celery worker -l info
celerybeat: celery -A  core beat -l INFO
