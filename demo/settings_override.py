SECRET_KEY="$_99bc($w4iv1h8qn=q5*g-gtb&99db+0kls8m6+avmzu8w^8x"
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8080', 'https://demo.silverstrike.org']
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'demo.silverstrike.org']
DEBUG = True
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'demo_middleware.AlwaysAuthenticatedMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
