import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'roshan_shop.settings')

celery = Celery('roshan_shop')
celery.config_from_object('django.conf:settings' , namespace='CELERY')
celery.autodiscover_tasks()