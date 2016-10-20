import os
import sys

PROJECT_DIR = os.path.dirname(__file__)

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'datetimewidget.tests.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'datetimewidget',
    'datetimewidget.tests',
]

DEFAULT_FILE_STORAGE = 'datetimewidget.storage.DatabaseStorage'

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# Disable migrations.
# http://stackoverflow.com/a/28560805/247542
class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"
SOUTH_TESTS_MIGRATE = False # <= Django 1.8
# if django.VERSION > (1, 7, 0): # > Django 1.8 
#     MIGRATION_MODULES = DisableMigrations()

USE_TZ = True

SECRET_KEY = 'secret'

AUTH_USER_MODEL = 'auth.User'

SITE_ID = 1

BASE_SECURE_URL = 'https://localhost'

BASE_URL = 'http://localhost'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Required for Django>=1.10.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '%s/templates' % PROJECT_DIR,
        ],
#         'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug': True,
        },
    },
]
