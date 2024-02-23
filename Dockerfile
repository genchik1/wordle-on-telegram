FROM nikolaik/python-nodejs:python3.11-nodejs20-slim

ARG SOURCES_DIR="src/"
ARG POETRY_VERSION=1.6.1

ENV PROJECT_VERSION=0.0.1

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN set -ex apt-get update
COPY pyproject.toml poetry.lock ./
ARG POETRY_GROUP=main
RUN set -ex \
    && npm install -g nodemon \
    && pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && pip install setuptools==68.1.2 \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction $(bash -c "if [ $POETRY_GROUP == 'dev' ]; then echo '--dev'; elif [ $POETRY_GROUP == 'web' ]; then echo '--only web';else echo '--only main'; fi}") \
    && rm -rf /root/.cache

WORKDIR /code

COPY ${SOURCES_DIR} /code/
COPY data/words.json /data/words.json
#COPY src/alembic.ini /code/alembic.ini
