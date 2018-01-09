PHONY: test devinstall flaketests

test: flaketests

devinstall:
	pip install -e .[dev]

flaketests:
	flake8
