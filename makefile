activate:
	pipenv shell

clean:
	rm -rf build/ dist/ horserace.egg-info/ .pytest_cache/ .tox/

static-analysis:
	flake8

tdd:
	pytest-watch

test-unit:
	tox -e py35

pre-commit: clean
	tox

run:
	python horserace/horserace.py

package:
	python setup.py bdist_wheel

show-coverage:
	python -m webbrowser htmlcov/index.html

install:
	pip install --upgrade .

# Use this to develop
deploy-develop:
	pip install --editable .
