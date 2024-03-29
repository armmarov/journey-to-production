.PHONY: init run_dev run_stage run_prod unit_test

create_venv:
	python3.8 -m venv venv

source_venv:
	source venv/bin/activate

init: source_venv
	pip install --upgrade pip && pip install -r requirements.txt

run_dev:
	export FLASK_ENV=Development && \
	export FLASK_RUN_PORT=5000 && \
	export FLASK_DEBUG=1 && \
	flask run

run_stage:
	export FLASK_ENV=Staging && \
	export FLASK_RUN_PORT=5000 && \
	export FLASK_DEBUG=1 && \
	flask run

run_prod:
	export FLASK_ENV=Production && \
	export FLASK_DEBUG=0 && \
	gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 120 --keep-alive 5 --log-level info

unit_test:
	export FLASK_ENV=Development && \
	export FLASK_RUN_PORT=5000 && \
	export FLASK_DEBUG=1 && \
	pytest -v

init_db:
	flask db init

migrate_db:
	flask db migrate