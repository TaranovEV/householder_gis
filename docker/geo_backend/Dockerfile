FROM python:3.10.5-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gdal-bin curl

ENV POETRY_HOME /opt/poetry
ENV POETRY_BIN $POETRY_HOME/bin/poetry
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==1.2.2

COPY ./geo_back/pyproject.toml ./geo_back/poetry.lock ./

RUN $POETRY_BIN config --local virtualenvs.create false
RUN $POETRY_BIN install --no-root


COPY ./geo_back/manage.py ./
COPY ./geo_back/pytest.ini ./
COPY ./geo_back/householder_gis ./householder_gis
COPY ./geo_back/static ./static
COPY ./.env ./
COPY ./geo_back/pytest.ini ./
