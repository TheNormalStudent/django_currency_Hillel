from settings.settings import *

DEBUG = False
CELERY_TASK_ALWAYS_EAGER = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ( # 401
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ( # 403
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'rates_anon_trottle': '100/min',
    },
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

EMAIL_HOST_USER = 'testmail@test.testcom'
SUPPORT_EMAIL = EMAIL_HOST_USER