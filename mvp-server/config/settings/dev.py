import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = secrets['DB_SETTINGS']
"""
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "postdb",
        "USER": "root",
        "PASSWORD": "112233",
        "HOST": "localhost",
        "PORT": "3306"
    }
}
"""