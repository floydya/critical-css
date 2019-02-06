start:
	gunicorn app.wsgi -b 0.0.0.0:8000 -c app/gunicorn.py

setup:
	apt-get install rabbitmq-server
	npm install
	pip install -r requirements.txt

requirements:
	pipenv shell
	pip freeze > requirements.txt
	deactivate
