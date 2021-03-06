# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.dev')

# bootstrap for worker
import bootstrap
bootstrap.bootstrap()

from django.conf import settings  # noqa

app = Celery(settings.PROJECT_NAME, broker=settings.BROKER_URL)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
