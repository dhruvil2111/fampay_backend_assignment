release: python manage.py migrate
web: gunicorn config.wsgi:applicationworker: REMAP_SIGTERM=SIGQUIT celery worker --app=config.celery_app --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery beat --app=config.celery_app --loglevel=info
