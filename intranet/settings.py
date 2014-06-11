"""
Django settings for intranet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append("/var/www/intranet/modules")
APPEND_SLASH = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '853lka=jk+81sq(*i8vh4#sq=3-+e(y2u1-9-t3j$ky=h+e3@)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_management',
    'forum',
    'news',
    'contact',
    'projects',
)

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
  "django.core.context_processors.request",
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.tz",
  "django.contrib.messages.context_processors.messages",
  "django.contrib.auth.context_processors.auth",
  'django.core.context_processors.csrf',

  )

ROOT_URLCONF = 'intranet.urls'

WSGI_APPLICATION = 'intranet.wsgi.application'

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql', 
       'NAME': 'intranet',
       'USER': 'root',
       'PASSWORD': '', 
       'HOST': 'localhost',
       'PORT': '3306',
   }
}
 
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = '/var/www/intranet/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/var/www/intranet/static/'
STATIC_URL = '/static/'
ADMINS = (
  ('Cedric Cervantes', 'cervantescedric@gmail.com'),
)
TEMPLATE_DIRS = (
  "/var/www/intranet/templates/v1"
)

LOGIN_URL = "/user/login/"
LOGIN_REDIRECT_URL = "/user/dashboard/"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, PosixGroupType

AUTH_LDAP_GLOBAL_OPTIONS = {
 ldap.OPT_X_TLS_REQUIRE_CERT: False,
 ldap.OPT_REFERRALS: False,
}
LDAP_USER = "" # entrez votre username
AUTH_LDAP_BIND_PASSWORD = "" # entrez votre mdp

AUTH_LDAP_SERVER_URI = "ldap://ldap.42.fr"
AUTH_LDAP_BIND_DN = "cn="+ LDAP_USER + ",ou=2013,ou=people,dc=42,dc=fr"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=2013,ou=people,dc=42,dc=fr", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=2013,ou=people,dc=42,dc=fr"
AUTH_LDAP_START_TLS = True
AUTH_LDAP_ALWAYS_UPDATE_USER = True

AUTHENTICATION_BACKENDS = ( 'django_auth_ldap.backend.LDAPBackend', 'django.contrib.auth.backends.ModelBackend',)
