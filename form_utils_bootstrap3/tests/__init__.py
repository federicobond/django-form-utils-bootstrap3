import os

import django
from django.conf import settings


if not settings.configured:
    settings_dict = dict(
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'bootstrap3',
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
        BOOTSTRAP3={
            'form_renderers': {
                'default': 'form_utils_bootstrap3.renderers.BetterFormRenderer'
            }
        }
    )

    if django.VERSION >= (1, 8):
        settings_dict['TEMPLATES'] = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': []
            }
        ]

    settings.configure(**settings_dict)

django.setup()
