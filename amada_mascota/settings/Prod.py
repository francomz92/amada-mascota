from .Base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
		'HOST': 'db_host',
		'PORT': 'db_port',
        'NAME': 'db_name',
		'USER': 'db_user',
		'PASSWORD': 'db_password',
    }
}

# Configuraciones de email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'user@email.com'
EMAIL_HOST_PASSWORD = ''