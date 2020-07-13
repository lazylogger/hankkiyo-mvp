import os
import json

# 현재 BASE_DIR 는  mvp-server
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'secrets.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

"""
ALLOWED_HOSTS = [
    '127.0.0.1',
    '*',
]
"""

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # api docs
    'drf_yasg',

    # third party
    'rest_framework',
    'storages',
    'pipeline',
    'corsheaders',
    # 'sentry_sdk',

    # my app
    'api',
]

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    'http://3.34.210.157:8000',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = secrets['DB_SETTINGS']


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

# USE_TZ = True   # 장고 내부적으로 인식하는 시간대
USE_TZ = False   # local time 사용


# PIPELINE
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'JAVASCRIPT': {
        'stats': {
            'source_filenames': (
              'js/jquery.js',
              'js/d3.js',
              'js/collections/*.js',
              'js/application.js',
            ),
            'output_filename': 'js/stats.js',
        }
    }
}

"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'   # Local, 즉 DEBUG=True 일 경우 pipeline 사용

    MEDIA_URL = '/media/'   # config/media/모델명/사진.jpg
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:
    # AWS S3 AWS Setting
    AWS_ACCESS_KEY_ID = secrets['AWS_S3']['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = secrets['AWS_S3']['AWS_SECRET_ACCESS_KEY']
    AWS_REGION = secrets['AWS_S3']['AWS_REGION']

    AWS_STORAGE_BUCKET_NAME = secrets['AWS_S3']['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = None

    # Static Setting
    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # Media Setting
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

""" 

# AWS S3 AWS Setting
AWS_ACCESS_KEY_ID = secrets['AWS_S3']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_S3']['AWS_SECRET_ACCESS_KEY']
AWS_REGION = secrets['AWS_S3']['AWS_REGION']

AWS_STORAGE_BUCKET_NAME = secrets['AWS_S3']['AWS_STORAGE_BUCKET_NAME']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = None

# Static Setting
STATIC_URL = '/static/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media Setting
# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

