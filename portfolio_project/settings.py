"""
Django settings for portfolio_project.
Minimal, single-app config for a personal portfolio site.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ Change this before deploying anywhere public, and keep it secret
# (e.g. load from an environment variable instead of hardcoding it).
SECRET_KEY = 'django-insecure-CHANGE-ME-before-deploying'

# Set to False in production
DEBUG = True

ALLOWED_HOSTS = ['*']  # ⚠️ Restrict this to your real domain(s) in production

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'portfolio',  # our app
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

ROOT_URLCONF = 'portfolio_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # APP_DIRS=True already looks inside portfolio/templates/,
        # this DIRS entry lets you add project-wide templates too if needed.
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

WSGI_APPLICATION = 'portfolio_project.wsgi.application'
ASGI_APPLICATION = 'portfolio_project.asgi.application'

# This portfolio doesn't need a database, but Django expects one configured.
# SQLite is fine — it won't even create a file unless you run migrate.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []  # no user-facing accounts on this site

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------------------
# STATIC FILES (css/js) — lives inside portfolio/static/portfolio/
# ---------------------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = []  # app-level static/ folders are picked up automatically
STATIC_ROOT = BASE_DIR / 'staticfiles'  # used by `collectstatic` for deployment

# ---------------------------------------------------------------------------
# MEDIA FILES — put your resume.pdf / profile photo here at runtime
# ---------------------------------------------------------------------------
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
