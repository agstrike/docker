SECRET_KEY="$_99bc($w4iv1h8qn=q5*g-gtb&99db+0kls8m6+avmzu8w^8x"
CSRF_TRUSTED_ORIGINS = ['demo.silverstrike.org']
ALLOWED_HOSTS = ['demo.silverstrike.org']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
