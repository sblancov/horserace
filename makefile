activate:
	pipenv shell

clean:
	rm -rf build/ dist/ horserace.egg-info/

static-analysis:
	flake8 horserace

run:
	python horserace/main.py

package:
	python setup.py bdist_wheel
