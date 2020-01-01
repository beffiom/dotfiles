

all: tests

FORCE:

tests: FORCE
	pytest-3

profile:
	./scripts/run_profile.py --profile-tool kcachegrind --profile-test tests/test_perf.py

mypy:
	mypy jmatrix

update-vendor:
	git subtree pull --prefix jblock/vendor/fpdomain fpdomain vendor --squash
