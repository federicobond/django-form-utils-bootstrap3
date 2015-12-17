import os

import django
from django.conf import settings


if not settings.configured:
    settings_dict = dict(
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'form_utils',
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        MEDIA_ROOT=os.path.join(os.path.dirname(__file__), 'media'),
        MEDIA_URL='/media/',
        STATIC_URL='/static/',
        MIDDLEWARE_CLASSES=[],
    )

    settings.configure(**settings_dict)


if django.VERSION >= (1, 7):
    django.setup()
