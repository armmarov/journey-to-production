.PHONY: init run_dev run_stage run_prod unit_test

create_venv:
	python3.8 -m venv venv

source_venv:
	source venv/bin/activate

init: source_venv
	pip install --upgrade pip && pip install -r requirements.txt

run_dev:
	export FLASK_ENV=Development && \
	export FLASK_RUN_PORT=5050 && \
	export FLASK_DEBUG=1 && \
	flask run

run_stage:
	export FLASK_ENV=Staging && \
	export FLASK_RUN_PORT=5050 && \
	export FLASK_DEBUG=1 && \
	flask run

run_prod:
	gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:3040 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info

unit_test:
	export FLASK_ENV=Development && \
	export FLASK_RUN_PORT=5050 && \
	export FLASK_DEBUG=1 && \
	pytest -v