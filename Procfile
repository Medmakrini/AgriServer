release: python manage.py migrate
web: gunicorn viableways.wsgi --bind 0.0.0.0:$PORT --log-file -
