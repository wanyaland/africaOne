"""
Django settings for africa_one project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$5l-f=#kfkj@jyv$o53q$23mm1dsdxa2ss7^v)rdp248ptt23+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'south',
    #'review',
    #'hvad',
    #'user_media',
    #'generic_positions',
    'social.apps.django_app.default',
    'geoposition',
    'admin',
    'djangoratings',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'africa_one.urls'

WSGI_APPLICATION = 'africa_one.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'africaone',
        'USER':'postgres',
        'PASSWORD':'africaone',
        'HOST':'localhost',
        'PORT':'',
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/media/'
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')

SOCIAL_AUTH_FACEBOOK_KEY = '1680902652194882'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ae1a5ac1caa8392bdd7198aee9f5f4b4'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='730951327557-rkje0er9bhpt1vuqod0isrhkcg74krhs.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='_zimvnPA7iLI2GFyau49Pp9p'
SOCIAL_AUTH_TWITTER_KEY = 'toQGgOTnxFXVB44O0ji38w7F5'
SOCIAL_AUTH_TWITTER_SECRET ='D1z9z3vCON830WHvINVmaI90mTzghvQSL1syrSBGvZqvGnrqLK'

AUTH_PROFILE_MODULE ='core.Customer'

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}
