SHELL=/bin/bash

# --------------
# Installation
# --------------
install:
	rm -rf env
	conda env create -f environment.yml --prefix ./env

# --------------
# Testing
# --------------
test: mypy pytest doctest  # run with -k flag in order to continue in case of recipe failure

mypy:
	mypy asciiplot/

pytest:
	coverage run -m pytest -vv tests/

doctest:
	python -m pytest -vv --doctest-modules --doctest-continue-on-failure ./asciiplot/


# --------------
# Building
# --------------
wheel:
	rm -rf asciiplot.egg-info
	rm -rf build
	python setup.py bdist_wheel --dist-dir ./dist
