from .base import *
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_NAME'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASS'),
        'HOST': env('MYSQL_HOST'),
        'PORT': env('MYSQL_PORT')
    }
}
