install:
    poetry install

update:
    poetry update

local: install
    poetry run pre-commit install

lint: ruff format

lint-fix: ruff-fix format-fix

ruff:
    poetry run ruff check

ruff-fix:
    poetry run ruff check --fix

format:
    poetry run ruff format --check

format-fix:
    poetry run ruff format

bandit:
    poetry run bandit -r animal_fact_api -q

safety:
    poetry run safety scan
