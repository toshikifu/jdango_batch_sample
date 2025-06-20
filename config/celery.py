import os
from celery import Celery
from django.conf import settings


os.environment.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app: Celery = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
