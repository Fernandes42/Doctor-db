release: python ./doctor_db/manage.py migrate
web: gunicorn --pythonpath doctor_db doctor_db.wsgi