SHELL=/bin/bash

# --------------
# Installation
# --------------
install:
	rm -rf env
	mamba env create -f environment.yml --prefix ./env

# --------------
# Testing
# --------------
test: mypy pytest doctest  # run with -k flag in order to continue in case of recipe failure

mypy:
	mypy asciiplot/

pytest:
	coverage run -m pytest -vv tests/
	coverage xml

doctest:
	python -m pytest -vv --doctest-modules --doctest-continue-on-failure ./asciiplot/


# --------------
# Building
# --------------
wheel:
	rm -rf asciiplot.egg-info
	rm -rf build
	rm -rf dist

	python setup.py sdist bdist_wheel --dist-dir ./dist

upload: wheel
	python -m twine check dist/*
	python setup.py sdist bdist_wheel upload
