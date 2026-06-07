run:
	python src/project_template/main.py

test:
	pytest

lint:
	ruff check .

check:
	pytest
	ruff check .
