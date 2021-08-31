import os
from pathlib import Path
import environ


env = environ.Env() #sayfama environment variable icindeki degiskenleri cekebilmeye yara
#environ.Env.read_env()
    #otomatik olarak manage.py nerede oldugunu saptar .env'i bulur ve bu environment degiskenlerini buradan okur
    #Secret kısmı yukarı aldım burda env ile koda ulascaz

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(os.path.join(BASE_DIR,'.env')) #Settingsleri development ve production olarak ayırdıktan sonra değiştirdik


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/






# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'blog',
    #3.parti applerim
    'ckeditor',
    'crispy_forms',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'




# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

AUTH_USER_MODEL = 'account.CustomUserModel'

MEDIA_URL = '/media/'
    
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')
    #media dosyamızın konumu, base_dir manage.py'in oldugu klasör

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'
    #login isleminden sonra anasayfaya git


#gmail_send/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'y.teker.1907.1907@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD') #past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS  = True
DEFAULT_FROM_EMAIL = 'y.teker.1907.1907@gmail.com'



#LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers':False, #jangonun default icindeki loggerları kaldırma
    'formatters': { #belli bir formatta log almak istersek
        'basit_ifade': {
            'format':'{asctime} {levelname} {message} {name}',
            'style': '{'
        }
    },
    'handlers':{
        'console':{
            'class':'logging.StreamHandler'
        },
        'file':{ #Dosyaya yazdırmak istersek
            'class': 'logging.FileHandler',
            'filename': 'logs/konu_okuma.log',
            'formatter': 'basit_ifade'
        }
    },    
    'loggers': {
        'konu_okuma': {
            'handlers': ['console','file'],
            'level': 'INFO'
        }
    }
}