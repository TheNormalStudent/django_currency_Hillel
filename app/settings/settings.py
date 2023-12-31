from pathlib import Path

from datetime import timedelta

from celery.schedules import crontab

from config import get_username_and_password_for_settings as get_info

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7j%+)xygq^u!egh*^(yr6hgwhmv$k#z@2g@x)gt)i#^5%y62i#'

# SECURITY WARNING: don't run with debug turned on in production!
# TODO move to env
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'silk',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'debug_toolbar',
    'rangefilter',
    'import_export',
    'crispy_bootstrap4',
    'crispy_forms',

    'currency',
    'rest_framework',
    'rest_framework_simplejwt',
    'api',
    'drf_yasg',
    'django_filters',


]

MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',

    'currency.middlewares.ResponseTimeMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'currency.middlewares.GclidMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / '..' / 'static_content' / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    '127.0.0.1',
]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
email_info = get_info()
EMAIL_HOST_USER = email_info['username']
EMAIL_HOST_PASSWORD = email_info['password']
SUPPORT_EMAIL = EMAIL_HOST_USER

CELERY_BROKER_URL = 'amqp://localhost'

CELERY_BEAT_SCHEDULE = {
    'parse_privat':
    {
        'task': 'currency.tasks.parse_privatbank',
        'schedule': crontab(minute='*/1'),
    },

    'parse_bank_com_ua':
    {
        'task': 'currency.tasks.parse_bank_com_ua',
        'schedule': crontab(minute='*/1'),
    },
        'parse_monobank':
    {
        'task': 'currency.tasks.parse_monobank',
        'schedule': crontab(minute='*/5'),
    },
        'parse_vkurse_dp':
    {
        'task': 'currency.tasks.parse_vkurse_dp',
        'schedule': crontab(minute='*/1')
    },
        'parse_minfin':
    {
        'task': 'currency.tasks.parse_minfin',
        'schedule': crontab(minute='*/1')
    },
}


AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

HTTP_SCHEMA = 'http'
DOMAIN = 'localhost:8000'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ( # 401
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ( # 403
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'rates_anon_trottle': '4/min',
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=14),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer', 'JWT'),
    'AUTH_HEADER_NAME': "HTTP_AUTHORIZATION",
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    
    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# LOGGING = {
#     'version': 1,
#     'filters' : {
#         'require_debug_true':{
#             '()':'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'console':{
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',}
#     },
#     'loggers': {
#         'django.db.backends':{
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }