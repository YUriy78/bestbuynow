"""
Django settings for bestbuynow project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4!=!*l)8b=jkdu)v)&^q-#5b53nin-i_$ow1b0_7w#po)*fc&f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [ 'best-buy-now.ru', 'www.best-buy-now.ru']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'board',
	'catalog',
	'burse',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bestbuynow.urls'

WSGI_APPLICATION = 'bestbuynow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'successf_bestbuynow',
        'USER': 'successf_yuriyd',
        'PASSWORD': '1356711xyWzabc',
        'HOST': '10.0.0.2',
        'PORT': '',
    }
}

MEDIA_ROOT = '/home/successf/domains/best-buy-now.ru/public_html/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/successf/domains/best-buy-now.ru/public_html/static/'
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
	'/home/successf/domains/best-buy-now.ru/public_html/templates',

)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_HOST = 'best-buy-now.ru'
EMAIL_HOST_USER = 'yuriy@best-buy-now.ru'
EMAIL_HOST_PASSWORD = '35xy35111538'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

