# Copyright (c) 2011-2015 Berkeley Model United Nations. All rights reserved.
# Use of this source code is governed by a BSD License (see LICENSE).
import os
from .roots import HUXLEY_ROOT, PROJECT_ROOT


DEBUG = os.environ.get('HUXLEY_DEBUG', True)
ALLOWED_HOSTS = [os.environ.get('HUXLEY_HOST', '')]
TEMPLATE_DEBUG = DEBUG

# IMPORTANT: Override this in local settings!
SECRET_KEY = '+42lz(cp=6t#dzpkah^chn760l)rmu$p&f-#7ggsde2l3%fm-i'

ADMINS = (('BMUN Tech Officer', 'tech@bmun.org'))
ADMIN_SECRET = 'OVERRIDE THIS IN PRODUCTION'
MANAGERS = ADMINS

SITE_ID = 1

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '%s/huxley.db' % HUXLEY_ROOT, # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('HUXLEY_DB_NAME', ''),
            'USER': os.environ.get('HUXLEY_DB_USER', ''),
            'PASSWORD': os.environ.get('HUXLEY_DB_PASSWORD', ''),
            'HOST': os.environ.get('HUXLEY_DB_HOST', ''),
            'PORT': os.environ.get('HUXLEY_DB_PORT', '')
        }
    }


ROOT_URLCONF = 'huxley.urls'

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = '%s/public/static/' % PROJECT_ROOT
STATIC_URL = '/static/'

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    '%s/templates/' % HUXLEY_ROOT,
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'huxley.core.middlewares.ExceptionLoggerMiddleware',
    'huxley.core.middlewares.ServerLoggingMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'huxley.accounts.backends.LoginAsUserBackend'
)

AUTH_USER_MODEL = 'accounts.User'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'huxley.core',
    'huxley.api',
    'huxley.accounts',
    'huxley.payments',
    'huxley.www',
    'huxley.logging',
    'pipeline',
)
