.PHONY: test
test: rufftest typingtest unittest

.PHONY: rufftest
rufftest:
	uv run ruff check .
	uv run ruff format --check .

.PHONY: rufffix
rufftest:
	uv run ruff check --fix-only .
	uv run ruff format .

.PHONY: typingtest
typingtest:
	uv run ty check

.PHONY: unittest
unittest:
	uv run coverage run -m unittest --durations 5
	uv run coverage report

.PHONY: clean
clean:
	rm -rf build dist

.PHONY: publish
publish:
	uv build
	uv publish

.PHONY: demo
demo:
	make -C demo/ demo
