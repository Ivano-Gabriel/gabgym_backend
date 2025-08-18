# gabgym_api/settings.py

import os
from pathlib import Path

# --- Configurações Básicas do Django ---
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' # Mantenha a sua chave secreta original
DEBUG = True
ALLOWED_HOSTS = []

# --- Aplicações Instaladas ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Necessário para allauth
    
    # Nossas Apps
    'api.apps.ApiConfig', # ou apenas 'api'

    # Apps de Terceiros
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'dj_rest_auth',
    'dj_rest_auth.registration', # Para o registro de novos usuários
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Deve vir antes de CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'gabgym_api.urls'
TEMPLATES = [ { 'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [], 'APP_DIRS': True, 'OPTIONS': { 'context_processors': [ 'django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth', 'django.contrib.messages.context_processors.messages', ], }, }, ]
WSGI_APPLICATION = 'gabgym_api.wsgi.application'

# --- Banco de Dados ---
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3', } }

# --- Validação de Senhas ---
AUTH_PASSWORD_VALIDATORS = [ { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', }, { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', }, { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', }, { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', }, ]

# --- Internacionalização ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Arquivos Estáticos ---
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CONFIGURAÇÕES DE CONEXÃO E SEGURANÇA ---
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True

# --- CONFIGURAÇÕES DAS APIS (REST FRAMEWORK & DJ-REST-AUTH) ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# Diz ao dj-rest-auth para usar o sistema de Token do DRF, e não JWT
REST_AUTH = {
    'USE_JWT': False,
}

# Garante que o Django use o sistema de autenticação do allauth (para login com email)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # Necessário para o admin do Django
    'allauth.account.auth_backends.AuthenticationBackend',
]

# --- CONFIGURAÇÕES DO ALLAUTH (SISTEMA DE USUÁRIOS) ---
SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'none' # Para simplificar nossos testes