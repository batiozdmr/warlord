"""
Django settings for core project.
Generated by 'django-admin startproject' using Django 3.0.8.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from pathlib import Path

from celery import Celery
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qkmseu9oximezobg5j6ux&t!b$2rn+thmtd^=a62r-jsu2)qp='
# Silinicek
AWS_ACCESS_KEY_ID = 'AKIAX72C3EPOIP27KWYD'
AWS_SECRET_ACCESS_KEY = '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'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'translations',
    'storages',
    'collectfast',
    'corsheaders',
    'modeltranslation',
    'django_celery_beat',
    'celery',
]

LOCAL_APPS = [
    'apps.parameter',
    'apps.mainpage',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.parameter.context_processors.menu',
                'apps.parameter.context_processors.site',
            ],
        },
    },
]

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcthmfnca8kr30',
        'USER': 'yzfuzuzkdlmgpd',
        'PASSWORD': '17ad012282741331801fadbfa7de81e1b0a169cae6ad65898a3836945294ebe3',
        'HOST': 'ec2-54-228-125-183.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'tr-Tr'
gettext = lambda s: s
LANGUAGES = (
    ('tr', gettext('Turkish')),
)
MODELTRANSLATION_LANGUAGES = ('tr',)
ROSETTA_SHOW_AT_ADMIN_PANEL = True

USE_TZ = True
TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

AWS_STORAGE_BUCKET_NAME = 'yardimaihtiyacimvar'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
# silinicek
AWS_S3_CUSTOM_DOMAIN = 'yardimaihtiyacimvar.s3.eu-central-1.amazonaws.com'
S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = S3_URL + '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = S3_URL + '/media/'

DEFAULT_FILE_STORAGE = 'core.s3_settings.MediaS3BotoStorage'
STATICFILES_STORAGE = 'core.s3_settings.StaticS3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = 'core.s3_settings.ThumbS3BotoStorage'
COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
COLLECTFAST_THREADS = 10

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
PERMISSION_DENIED_PAGE_URL = '/403/'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = os.path.join(STATIC_URL, 'assets/plugins/jquery.min.js')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'tr'
DATE_INPUT_FORMATS = ['%d/%m/%Y']
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

CKEDITOR_ALLOW_NONIMAGE_FILES = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_CREDENTIALS = True
# SECURE_SSL_REDIRECT = True

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}

# Celery base setup
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
