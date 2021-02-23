export DJANGO_SECRET_KEY=''
export DJANGO_DEBUG=1

export DJANGO_DB_ENGINE='django.db.backends.postgresql'
export DJANGO_DB_NAME=''
export DJANGO_DB_USER=''
export DJANGO_DB_PASSWORD=''
export DJANGO_DB_HOST=''
export DJANGO_DB_PORT=''

export DJANGO_LOG_LEVEL='INFO'

export DJANGO_SUPERUSER_USERNAME=''
export DJANGO_SUPERUSER_EMAIL=''
export DJANGO_SUPERUSER_PASSWORD=''

export GOOGLE_RECAPTCHA_SECRET_KEY=''
export GOOGLE_RECAPTCHA_SITE_KEY=''

cd gtm_demo_web

python manage.py create_postgres_db
python manage.py makemigrations
python manage.py migrate
python manage.py init_superuser
python manage.py collectstatic --noinput
python manage.py runserver