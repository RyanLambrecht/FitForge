"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 5.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from environs import Env
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Make sure you've initialized the `env` object!
FORCE_SCRIPT_NAME = (
	'/' + env.str('SITE_NAME', default=None)  # if the SITE_NAME env variable is set
	if not env.str('SITE_NAME', default=None) # if not
	else ''  # set to nothing to let Django take over
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# load the key; use default if key var not set
SECRET_KEY = env.str('SECRET_KEY', default='django-insecure-4$6@5&r4%kex2%me935-8q^=ep=ufnyv89&i7@dx^68924o2q#')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool(
	'DEBUG',
	default=False  # or True, to fail unsafely
)

ALLOWED_HOSTS = [
	'localhost',
	'127.0.0.1',
	'csci258.cs.umt.edu',  # this is the url of the VM
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "debug_toolbar",
    "workouts",
    "nutrition",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # For a global template directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
	# PostgreSQL database used in production
	'prod': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': env.str('POSTGRES_DB', default=None),
		'USER': env.str('POSTGRES_USER', default=None),
		'PASSWORD': env.str('POSTGRES_PASSWORD', default=None),
		'HOST': 'postgres',
		'PORT': '5432',
	},

	# local SQLite database used for development and testing
	'local': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}

	# any other configs would go down here
}


# defaults to local if not set in environment variable
# environment variable is set by the Docker config
default_database = env.str('DJANGO_DATABASE', default='local')
# sets detected database to default
DATABASES['default'] = DATABASES[default_database]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# URL path to serve static files from; ex: '/group1/static/'
STATIC_URL = FORCE_SCRIPT_NAME + '/static/'

# project static files location
STATICFILES_DIRS = [ BASE_DIR / "static" ]

# collected static files location; includes other apps, like admin
STATIC_ROOT = BASE_DIR / 'staticfiles'

# enable caching and compression when serving static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"


INTERNAL_IPS = [
	'127.0.0.1',
	'localhost',
]

DEBUG_TOOLBAR_CONFIG = {
    "INSERT_BEFORE": "</body>",
}