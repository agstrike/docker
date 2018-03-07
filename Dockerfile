FROM python:slim-stretch

# Install mysql client
RUN apt-get update && apt-get install -y gcc

# install deps
RUN pip install --no-cache-dir silverstrike whitenoise uwsgi psycopg2-binary dj-database-url

RUN apt-get remove -y gcc

# Copy the code
RUN mkdir /code
WORKDIR /code

ADD . /code

# configure django
ENV DJANGO_SETTINGS_MODULE=settings

# configure uwsgi
ENV UWSGI_WSGI_FILE=wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# collect static files
RUN python manage.py collectstatic

CMD sleep 5 && python manage.py migrate && uwsgi
