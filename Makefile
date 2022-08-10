SHELL=/bin/bash

test: mypy pytest doctest coverage-report  # run with -k flag to continue in case of recipe failure

mypy:
	mypy asciiplot/

pytest:
	coverage run -m pytest -vv tests/

doctest:
	coverage run -am pytest -vv --doctest-modules --doctest-continue-on-failure ./asciiplot/

coverage-report:
	coverage xml
	coverage report

coverage-html:
	coverage html
	firefox htmlcov/index.html