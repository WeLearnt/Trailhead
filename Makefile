.PHONY: setup check test test-standin test-trailhead

PYTHON ?= python3
STANDIN := examples/pandas-standin

setup:
	bash scripts/trailhead-setup.sh

check:
	$(PYTHON) scripts/trailhead-check.py --verify-manifest $(STANDIN)

test-standin:
	cd $(STANDIN) && PYTHONPATH=. $(PYTHON) -m pytest pandas/tests/ -q

test-trailhead:
	$(PYTHON) -m pytest tests/ -q

test: check test-standin test-trailhead
