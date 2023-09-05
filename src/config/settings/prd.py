from config.settings.base import *  # NOQA

DEBUG = False

SECRET_KEY = 'django-insecure-3p+sh-46d!zu9fopoktbq#nrc6^^tvegxez_5)%z_-0hzl9(&b'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # NOQA
    }
}

STATIC_URL = 'static/'
