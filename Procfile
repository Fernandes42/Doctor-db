release: python --pythonpath doctor-db manage.py migrate
web: gunicorn --pythonpath doctor_db doctor_db.wsgi