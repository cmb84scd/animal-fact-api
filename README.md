# Animal Fact API

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![security: safety](https://img.shields.io/badge/security-safety-blue)](https://github.com/pyupio/safety)
[![Pipeline CI](https://github.com/cmb84scd/animal-fact-api/actions/workflows/pipeline.yml/badge.svg)](https://github.com/cmb84scd/animal-fact-api/actions?query=branch:main)
![Code Coverage](https://img.shields.io/badge/Code%20Coverage-100%25-success?style=flat)

- [Overview](#overview)
- [Setup](#setup)
  - [Python](#python)
  - [Poetry](#poetry)
  - [Just](#just)
  - [PostgreSQL](#postgresql)
  - [Project](#project)
- [Commands](#commands)

## Overview

Animal Fact API is a basic API that returns some animal facts and is built using Django. I created this as I wanted something to return some random facts as part of my learning, and I'm hoping to use it with another service.

## Setup

To use this project, you will need to have the following installed.

### Python

This project uses Python version 3.12. It is advised to use [pyenv](https://github.com/pyenv/pyenv) to install Python using:

```bash
pyenv install
```

### Poetry

This project uses poetry version 1.8.3. To install poetry, follow the instructions [here](https://python-poetry.org/docs/) or to update it if you already have it installed run:

```bash
poetry self update
```

### Just

This project uses just to run the lint, test, etc commands. To use just you will need to install it but if you'd prefer not to, you can copy the commands from the `justfile` and paste them directly into your terminal to run them. To install just, follow the instructions [here](https://just.systems/man/en/).

### PostgreSQL

This project uses PostgreSQL version 14. To install PostgreSQL, follow the instructions [here](https://www.postgresql.org/download/).

### Project

Having installed the above, you can now clone the repository and install the dependencies, including Django, along with the pre-commit hook:

```bash
git clone git@github.com:cmb84scd/animal-fact-api.git
cd animal-fact-api
just local
```

Next, you need to create the database for this project. You can do this using `createdb <DB_NAME>`, replacing `<DB_NAME>` with the name of your database. It should be noted that, depending on your local set up, you might need to log into postgres first before creating the database.

Before you can run the database migrations, you will need to create a `.env` file and put the following in it:

```bash
SECRET_KEY='your-key'
DB_USERNAME='your-username'
DB_PASSWORD='your-password'
DB_NAME='your-db-name'
```

Replace the values with your details. For the `SECRET_KEY` you could use [djecrety](https://djecrety.ir/) to create one. Django needs this to run and generates one by default when you create a new project but it's wise to rotate this on a regular basis.

Once you have done this, you can run the migrations using `just migrate`.

Now you are ready to use the project! Once you've added some animal facts of your choice to your database, you can run `just run` to start the server. Then go to `localhost:8000/facts` to see a random fact. Check out [urls.py](animal_fact_api/facts/urls.py) for the other urls you can access.

### Commands

All commands are defined in the `justfile` and are run as `just {command}` where `{command}` is one of:

| Name     | Description                            |
| ----     | -------------------------------------- |
| test     | Runs all the unit tests                |
| test-cov | Runs all the unit tests with coverage  |
| lint     | Runs all the linting checks            |
| lint-fix | Automatically fixes any linting issues |

I haven't listed all the commands here, but you can see them all by looking in the `justfile`.
