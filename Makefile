.PHONY init

create_venv:
	python3.8 -m venv venv

source_venv:
	source venv/bin/activate

init: source_venv
	pip install --upgrade pip && pip install -r requirements.txt