install:
	pip install -e .
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C --ignore-patterns=tests/test_.*?py *.py lib/*.py

format:
	black lib main.py tests

refactor:
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r lib main.py tests

test:
	python -m pytest -vv --cov=main --cov=lib tests/test_*.py

clean:
	rm -rf __pycache__ .pytest_cache .coverage coverage.xml dist build *.egg-info
