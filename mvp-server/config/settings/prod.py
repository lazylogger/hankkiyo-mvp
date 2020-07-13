import os
from .base import *
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False  # 필수

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

DATABASES = secrets['DB_SETTINGS']

"""
sentry_sdk.init(
    dsn="https://d2d9bedaad6e4213af399af84af2e212@o419884.ingest.sentry.io/5337035",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
"""

