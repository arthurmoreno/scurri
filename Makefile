

run1to100:
	@python 1to100/onetohundred.py

tests:
	@pytest -s

cov1to100:
	@pytest -s --cov=1to100 --cov-report html
	@coverage-badge -o coverage_1to100.svg

covpc:
	@pytest -s --cov=ukpostcodes --cov-report html
	@coverage-badge -o coverage_pc.svg

coverage: cov1to100 covpc
