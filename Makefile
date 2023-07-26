SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver

migrate:
	$(manage_py) app/manage.py migrate

worker:
	cd app && celery -A settings worker -l info

shell:
	$(manage_py) shell_plus --print-sql

beat:
	cd app && celery -A settings beat -l info