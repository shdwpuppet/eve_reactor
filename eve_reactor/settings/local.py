import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "{{ db_name }}",
        'USER': "{{ db_user }}",
        'PASSWORD': "{{ db_password }}",
    }

}

SHARE_URL = "http://127.0.0.1:8000"
# Static assets
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)
# User uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')