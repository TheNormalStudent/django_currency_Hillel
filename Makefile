SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) app/manage.py migrate

worker:
	cd app && celery -A settings worker -l info
