import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(__file__)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DOMAINS AND URLS
SERVER_DOMAIN = ''
ALLOWED_HOSTS = ['*']
LOGIN_URL = '/login/'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
DATETIME_FORMAT = 'Y-m-d H:i:s e'
USE_I18N = True
USE_L10N = False
USE_TZ = True

# MISC
CRISPY_TEMPLATE_PACK = 'bootstrap3'
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auth',
        'USER': os.environ.get('AA_DB_DEFAULT_USER', 'auth'),
        'PASSWORD': os.environ.get('AA_DB_DEFAULT_PASSWORD', 'somepassword'),
        'HOST': os.environ.get('AA_DB_DEFAULT_HOST', 'db'),
        'PORT': os.environ.get('AA_DB_DEFAULT_PORT', '3306'),
    },
}


# INSTALLED APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'crispy_forms',
    'core',
    'modules.discord',
    'modules.discourse',
    'modules.engagement',
    'modules.eveonline',
    'modules.applications',
]

# EXTENSIONS
# Warning: Extensions are difficult to disable and re-enable, it requires dropping SQL tables and rerunning migrations.
# This is because they create dependencies because they rely on other modules. 
INSTALLED_APPS += [
    'modules.eveonline.extensions.eveaudit',
    'modules.eveonline.extensions.evedoctrine',
]

# APPLCATION DEFINITION
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'core/templates',
            'eveonline/templates',
            'hrapplications/templates',
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.installed_apps',
                'core.context_processors.social_media_objects',
                'core.context_processors.get_application_verbose_names',
                'core.context_processors.get_google_analytics_code',
                'core.context_processors.get_site_logo',
                'core.context_processors.get_site_title',
                'core.context_processors.get_breadcrumbs',
		'core.context_processors.get_forum_url',
            ],
        },
    },
]

# PASSWORD VALIDATION
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

"""
Library Configuration
These configuration values are from libraries that require settings.py values.
"""
# SMTP
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''

# LOGGING
"""
When editing logger levels, change the HANDLERS only.
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M"
        }
    },
    'handlers': {
        'main': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/logs/main.log',
            'formatter': 'standard'
        },
        'core': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/logs/core.log',
            'formatter': 'standard'
        },
        'eveonline': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/logs/eveonline.log',
            'formatter': 'standard'
        },
        'discord': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/logs/discord.log',
            'formatter': 'standard'
        },
        'discourse': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/logs/discourse.log',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['main'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['main'],
            'level': 'DEBUG',
        },
        'core': {
            'handlers': ['main'],
            'level': 'DEBUG',
        },
        'modules.discourse': {
            'handlers': ['discourse'],
            'level': 'DEBUG',
        },
        'modules.discord': {
            'handlers': ['discord'],
            'level': 'DEBUG',
        },
        'games.eveonline': {
            'handlers': ['eveonline'],
            'level': 'DEBUG',
        },
    },
}

# SHELL PLUS
SHELL_PLUS_PRE_IMPORTS = [
    ('core.models', '*'),
    ('core.tasks', '*')
]
if "modules.discourse" in INSTALLED_APPS:
    SHELL_PLUS_PRE_IMPORTS.append(('modules.discourse.models', '*'))
    SHELL_PLUS_PRE_IMPORTS.append(('modules.discourse.tasks', '*'))
if "modules.discord" in INSTALLED_APPS:
    SHELL_PLUS_PRE_IMPORTS.append(('modules.discord.models', '*'))
    SHELL_PLUS_PRE_IMPORTS.append(('modules.discord.tasks', '*'))
if "modules.guild" in INSTALLED_APPS:
    SHELL_PLUS_PRE_IMPORTS.append(('modules.guild.models', '*'))
    SHELL_PLUS_PRE_IMPORTS.append(('modules.guild.tasks', '*'))
if "modules.eveonline" in INSTALLED_APPS:
    SHELL_PLUS_PRE_IMPORTS.append(('modules.eveonline.models', '*'))
    SHELL_PLUS_PRE_IMPORTS.append(('modules.eveonline.tasks', '*'))
