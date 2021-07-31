.PHONY: demo test devinstall flaketests checkmanifest checksetup clean build release

demo:
	timelapse --name ./demo/S60_050504 --pattern "./demo/source/*.jpg" --fps 25 --deflicker 7 --quiet

test: flaketests checkmanifest checksetup

devinstall:
	pip install --upgrade --upgrade-strategy eager -e .[dev]

flaketests:
	flake8

checksetup:
	python setup.py check -ms

clean:
	rm -rf build dist

build: test clean
	python setup.py sdist bdist_wheel
	twine check dist/*

release: build
	twine upload dist/*
