
activate:
	pipenv shell

analyze-security:
	bandit -r horserace

bumpversion:
	bumpversion

cobertura:
	pytest --cov=horserace --cov-report html tests/unit/

clean:
	rm -rf build/ dist/ horserace.egg-info/ .pytest_cache/ .tox/
	rm -rf htmlcov/ .coverage
	find . -name __pycache__ | xargs rm -rf

deploy-develop:
	pip install --editable .

generate-changelog:
	auto-changelog

package:
	python setup.py bdist_wheel

pre-push: clean static-analysis test-unit

run:
	python horserace/horserace.py

show-coverage:
	python -m webbrowser htmlcov/index.html

startup:
	pip install -r requirements.txt
	pipenv install --dev

static-analysis:
	flake8

tdd:
	pytest-watch

test-unit:
	pytest --cov horserace --cov-report term-missing tests/unit/
