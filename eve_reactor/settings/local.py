import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
    }

}

SHARE_URL = "http://127.0.0.1:8000"
# Static assets
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# User uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')