

run1to100:
	@python 1to100/onetohundred.py

test1to100:
	@pytest -s --cov=1to100 --cov-report html

testpc:
	@pytest -s --cov=ukpostcodes --cov-report html
