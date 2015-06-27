import os
from settings_base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Allow all host headers
ALLOWED_HOSTS = ['*']
