.PHONY: devinstall
devinstall:
	pip install --upgrade pip
	pip install --upgrade --upgrade-strategy eager --editable .[dev]

.PHONY: test
test: flaketest checksetup unittests

.PHONY: flaketest
flaketest:
	flake8

.PHONY: checksetup
checksetup:
	python setup.py check -ms

.PHONY: unittests
unittests:
	python -m unittest discover --catch --start-directory tests --top-level-directory .

.PHONY: clean
clean:
	rm -rf build dist

.PHONY: build
build: test clean
	python -m build --sdist --wheel
	twine check dist/*

.PHONY: release
release: build
	twine upload dist/*

.PHONY: demo
demo:
	make -C demo/ demo
