activate:
	pipenv shell

clean:
	rm -rf build/ dist/ horserace.egg-info/ .pytest_cache/ .tox/
	rm -rf htmlcov/ .coverage
	find . -name __pycache__ | xargs rm -rf

static-analysis:
	flake8

tdd:
	pytest-watch

test-unit:
	pytest tests/unit/

run:
	python horserace/horserace.py

package:
	python setup.py bdist_wheel

show-coverage:
	python -m webbrowser htmlcov/index.html

install:
	pip install --upgrade .

bumpversion:
	bumpversion

generate-changelog:
	auto-changelog

analyze-security:
	bandit -r horserace

pre-commit: clean static-analysis test-unit

deploy-develop:
	pip install --editable .
