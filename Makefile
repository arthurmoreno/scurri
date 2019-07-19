

run1to100:
	@python 1to100/onetohundred.py

tests:
	@pytest -s --cov=1to100 --cov-report html
