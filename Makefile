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
build: test
	rm -rf asciiplot.egg-info
	rm -rf build
	rm -rf dist

	python setup.py sdist bdist_wheel --dist-dir ./dist

upload: build
	python -m twine check dist/*
	python setup.py sdist bdist_wheel upload
