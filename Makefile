PHONY: test devinstall flaketests checkmanifest checksetup clean build release

test: flaketests checkmanifest checksetup

devinstall:
	pip install -e .[dev]

flaketests:
	flake8

checkmanifest:
	# Check if all files are included in the sdist
	check-manifest

checksetup:
	# Check longdescription and metadata
	python setup.py check -msr

clean:
	# Remove build/dist dirs
	rm -rf build dist

build: test clean
	# Test, clean and build
	python setup.py sdist bdist_wheel

release: build
	twine upload dist/*
