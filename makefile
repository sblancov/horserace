activate:
	pipenv shell

static-analysis:
	flake8 horserace

run:
	python horserace/main.py
