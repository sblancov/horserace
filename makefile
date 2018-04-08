activate:
	pipenv shell

clean:
	rm -rf build/ dist/ horserace.egg-info/ .pytest_cache/ .tox/

static-analysis:
	flake8 horserace

test-unit:
	tox -e py35

run:
	python horserace/main.py

package:
	python setup.py bdist_wheel
