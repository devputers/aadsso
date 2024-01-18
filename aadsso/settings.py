"""
Django settings for aadsso project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9dkl3#a7ko^(4b)j4v9(3@j6h+=l7%dpr3js@j06&ne2^xey%x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

SHARED_APPS = [
    'django_tenants',
    'aadsso_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'entra_auth'
]

TENANT_APPS = ['webUI']

INSTALLED_APPS = SHARED_APPS + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aadsso.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aadsso.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# DATABASES = {
#     "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR/"db.sqlite3"},
#     "dev": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR/"dev.sqlite3"},
#     "puters": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR/"puters.sqlite3"},
# }

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'aadsso_db',
        'USER': 'admin_postgres',
        'PASSWORD': 'admin_postgres',
        'HOST': 'localhost',  # Set to your PostgreSQL server's address
        'PORT': '5432',      # Set to your PostgreSQL server's port
    },
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TENANT_MODEL = "aadsso_app.Client"

TENANT_DOMAIN_MODEL = "aadsso_app.Domain"

PUBLIC_SCHEMA_URLCONF = "aadsso_app.urls"


# TODO: Add the MICROSOFT authentication credentials
ENTRA_CREDS = {
    "app_id": "f191eba3-fbf1-4f14-b843-",
    "app_secret": "Oj78Q~pX9qF0f4PlkxxdLIkayVzzmURQeOYuTduE",
    "redirect": "http://localhost:8080/entra_auth/callback",
    "scopes": ['User.Read'],
    "authority": "https://login.microsoftonline.com/acda4430-1c93-4d80-bd91-2af796c0c185",
    "valid_email_domains": ["chintannetsquare.onmicrosoft.com"],
    "logout_uri": "http://localhost:8080/admin/logout"
}
LOGIN_URL = "/entra_auth/login"
# LOGIN_REDIRECT_URL = "/entra_access"
LOGIN_REDIRECT_URL = "/dashboard"
