import os
from pathlib import Path

# ✅ Đường dẫn gốc của project
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Bảo mật và debug
SECRET_KEY = 'django-insecure-8jfgj$r+rqs#of%8g8(-&$vrutbqvd=$ll$&2@xtdow_592&it'
DEBUG = True  # ❗ Trong quá trình phát triển, luôn để True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Có thể thêm domain khi deploy

# ✅ Ứng dụng được cài đặt
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'landing',              # app của bạn
    'widget_tweaks',        # tùy chọn
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ Định tuyến gốc
ROOT_URLCONF = 'gout_landing.urls'

# ✅ Cấu hình templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # nơi chứa base.html hoặc index.html
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

WSGI_APPLICATION = 'gout_landing.wsgi.application'

# ✅ Cơ sở dữ liệu SQLite (có thể thay nếu cần)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Kiểm tra mật khẩu
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Ngôn ngữ và múi giờ
LANGUAGE_CODE = 'vi'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = True

# ✅ Static files (CSS, JS, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'landing' / 'static',  # đường dẫn tới thư mục chứa ảnh
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # nơi collectstatic gom vào

# ✅ Media files (nếu bạn có upload ảnh)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Email cấu hình (tuỳ chọn)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'landingpage1402@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'ufkj xyiq dcem jurc')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ✅ Trường mặc định cho model mới
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
