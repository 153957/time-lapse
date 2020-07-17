PHONY: test devinstall flaketests checkmanifest checksetup clean build release

test: flaketests checkmanifest checksetup

devinstall:
	pip install --upgrade --upgrade-strategy eager -e .[dev]

flaketests:
	flake8

checkmanifest:
	check-manifest

checksetup:
	python setup.py check -ms

clean:
	rm -rf build dist

build: test clean
	python setup.py sdist bdist_wheel
	twine check dist/*

release: build
	twine upload dist/*
