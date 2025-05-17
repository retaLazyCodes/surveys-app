lint:
	poetry run flake8 src/ tests/

format:
	poetry run black src/ tests/
