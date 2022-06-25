import os
from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['amikomers-django.herokuapp.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Ref: https://devcenter.heroku.com/articles/django-assets
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MIDDLEWARE += (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ALLOWED_ORIGINS = [
    'https://amikomers-vue.vercel.app',
    'https://amikomers.com',
]
