activate:
	pipenv shell

clean:
	rm -rf build/ dist/ horserace.egg-info/ .pytest_cache/ .tox/

static-analysis:
	tox -e flake8

test-unit:
	tox -e py35

pre-commit: clean
	tox

run:
	python horserace/main.py

package:
	python setup.py bdist_wheel

show-coverage:
	python -m webbrowser htmlcov/index.html
