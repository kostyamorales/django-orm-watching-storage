import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get("HOST"),
        'PORT': os.environ.get("PORT"),
        'NAME': os.environ.get("NAME"),
        'USER': os.environ.get("MY_APP_USER"),
        'PASSWORD': os.environ.get("PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
