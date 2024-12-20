
ALLOWED_HOSTS = ['F1ckzArd.pythonanywhere.com']


ALLOWED_HOSTS = ['.herokuapp.com']
STATIC_URL = '/static/'
STATIC_ROOT = '/home/F1ckzArd/BROclinic/static'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/F1ckzArd/BROclinic/static'  



from .martor_editor_settings import *
import os
from pathlib import Path
from django.conf.global_settings import EMAIL_HOST_PASSWORD, EMAIL_PORT


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-+&@h)&m+hy_wl&e4spf%u7xv=zj%bp=-h-cs^o*)@2d_g_7v8#"

DEBUG = True

if DEBUG:
    from dotenv import load_dotenv
    load_dotenv(".env")

ALLOWED_HOSTS = ["*"]



INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "martor",
    "active_link",
    "main",
    "docs",
    "authentication",
    "articles"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}



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



LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Almaty"

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = Path.joinpath(BASE_DIR, 'static')
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




if os.getenv("EMAIL_HOST_USER"):
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True

LOGIN_URL = '/login'
AUTH_USER_MODEL = "authentication.CustomUser"
