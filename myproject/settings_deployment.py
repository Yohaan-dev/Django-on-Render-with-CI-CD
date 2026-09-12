import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

# ==================== SECURITY ====================

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME', '')
ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME] if RENDER_EXTERNAL_HOSTNAME else []

CSRF_TRUSTED_ORIGINS = (
    [f'https://{RENDER_EXTERNAL_HOSTNAME}'] if RENDER_EXTERNAL_HOSTNAME else []
)

# Security headers for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

# ==================== MIDDLEWARE ====================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

# ==================== STATIC & MEDIA FILES ====================

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# ✅ FIXED: Use Cloudinary for media files
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

STORAGES = {
    "default": {
        # ✅ FIXED: Use Cloudinary for images
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ==================== DATABASE ====================

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
    )
}

# ==================== EMAIL ====================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # ✅ FIXED: No comma
EMAIL_HOST = 'smtp.gmail.com'  # ✅ FIXED: No comma
EMAIL_PORT = 587  # ✅ FIXED: No comma
EMAIL_USE_TLS = True  # ✅ FIXED: No comma
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')  # ✅ FIXED: No comma
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')  # ✅ FIXED: No comma
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_USER', 'noreply@example.com')  # ✅ FIXED: Use env var