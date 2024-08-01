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
    poetry run ruff format --diff

format-fix:
    poetry run ruff format

bandit:
    poetry run bandit -r animal_fact_api -q

safety:
    poetry run safety scan

test:
    poetry run coverage run --omit='manage.py' manage.py test animal_fact_api.tests.unit_tests
    poetry run coverage report -m --skip-covered && poetry run coverage html -d reports
    poetry run coverage xml -o reports/coverage.xml --fail-under=95

utest:
    poetry run python manage.py test animal_fact_api.tests.unit_tests

run:
    poetry run python manage.py runserver

make-migrations app:
    poetry run python manage.py makemigrations {{app}}

migrate:
    poetry run python manage.py migrate
