start:
	gunicorn app.wsgi -b 0.0.0.0:8000 -c app/gunicorn.py
