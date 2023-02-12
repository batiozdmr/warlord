from __future__ import absolute_import, unicode_literals

from celery import shared_task


@shared_task(name="data_checking")
def data_add():
    print(' Hello world')
    return 'test'
