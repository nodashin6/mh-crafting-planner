FROM weastur/poetry:1.8.3-python-3.12.4-bookworm

WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN poetry install