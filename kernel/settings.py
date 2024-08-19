from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-awdik+&kt%p(yi)z7-#x49^-+%y%)62va^b$1#3^00y$1dcl_='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
ALLOWED_HOSTS = ["78.157.51.34", "49.13.232.71", "127.0.0.1", "localhost"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'warehouse',
    'shop',
    'account',
    'services',
    'services.otp',
    'services.payment',
    'painless',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_extensions',
    'drf_yasg',
    'corsheaders',
    "azbankgateways",
    # "sep_payment"
    # 'django_filters',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kernel.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'kernel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME", "Backend"),
#         "USER": os.getenv("DB_USER", "Backend_user"),
#         "PASSWORD": os.getenv("DB_PASSWORD", "sdjnnfejsajad3574nndfkd"),
#         "HOST": os.getenv("DB_HOST", "db"),  # Updated to use the service name 'db'
#         "PORT": "5432",
#         "TEST": {"NAME": "Backend_test"},
#     },
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Backend",
        "USER": "Backend_user",
        "PASSWORD": "sdjnnfejsajad3574nndfkd",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "TEST": {"NAME": "Backend_test"},
    },
}


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

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Optionally, set the default timeout for keys
CACHE_TTL = 180  # 2 minutes

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'amieseansi@gmail.com'
EMAIL_HOST_PASSWORD = 'qblg uvce gdzg frzc'


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'debug.log'),
#             'formatter': 'verbose',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'services.otp': {  # Replace 'your_app_name' with the actual name of your app
#             'handlers': ['file', 'console'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     },
# }


AZ_IRANIAN_BANK_GATEWAYS = {
    "GATEWAYS": {
        # "BMI": {
        #     "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        #     "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
        #     "SECRET_KEY": "<YOUR SECRET CODE>",
        # },
        # "SEP": {
        #     "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        #     "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
        # },
        "IDPAY": {
            "MERCHANT_CODE": "6a7f99eb-7c20-4412-a972-6dfb7cd253a4",
            "METHOD": "POST",  # GET or POST
            "X_SANDBOX": 1,  # 0 disable, 1 active
        },
        # "ZARINPAL": {
        #     "MERCHANT_CODE": "6a7f99eb-7c20-4412-a972-6dfb7cd253a4",
        #     "SANDBOX": 1,  # 0 disable, 1 active
        # },
        # "ZIBAL": {
        #     "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        # },
        # "BAHAMTA": {
        #     "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        # },
        # "MELLAT": {
        #     "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
        #     "USERNAME": "<YOUR USERNAME>",
        #     "PASSWORD": "<YOUR PASSWORD>",
        # },
        # "PAYV1": {
        #     "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        #     "X_SANDBOX": 1,  # 0 disable, 1 active
        # },
    },
    "IS_SAMPLE_FORM_ENABLE": True,  # اختیاری و پیش فرض غیر فعال است
    "DEFAULT": "IDPAY",
    "CURRENCY": "IRR",  # اختیاری
    "TRACKING_CODE_QUERY_PARAM": "tc",  # اختیاری
    "TRACKING_CODE_LENGTH": 16,  # اختیاری
    "SETTING_VALUE_READER_CLASS": "azbankgateways.readers.DefaultReader",  # اختیاری
    "BANK_PRIORITIES": ["IDPAY"],
    #     "BMI",
    #     "SEP",
    #     # and so on ...
    # ],  # اختیاری
    "IS_SAFE_GET_GATEWAY_PAYMENT": False,  # اختیاری، بهتر است True بزارید.
    "CUSTOM_APP": None,  # اختیاری
}


# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     "78.157.51.34",
#     "49.13.232.71",
#     "127.0.0.1",
#     "localhost"
# ]
# CORS_ALLOW_METHODS = [
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# ]
# CORS_ALLOW_HEADERS = [
#     "accept",
#     "authorization",
#     "content-type",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# ]
# CORS_ALLOW_CREDENTIALS = True
# CORS_EXPOSE_HEADERS = [
#     "Content-Type",
#     "X-CSRFToken",
# ]
# CORS_ORIGIN_REGEX_WHITELIST = [
#     r"^https://\w+\.78.157.51.34:8000\.com$",
# ]


# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SAMESITE = 'Lax'
# SESSION_COOKIE_SECURE = False
# SESSION_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SAMESITE = 'Lax'

SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"


MERCHANT = "00000000-0000-0000-0000-000000000000"

SANDBOX = True
