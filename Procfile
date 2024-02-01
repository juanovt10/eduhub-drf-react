release: python manage.py makemigrations && python manage.py migrate
web: gunicorn eduhub_drf_api.wsgi