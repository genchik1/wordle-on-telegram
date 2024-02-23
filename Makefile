DOCKER_COMPOSE_PROJECT=wordle
DOCKER_COMPOSE_FILE_DEV="`pwd`/dev/docker-compose.dev.yml"
DOCKER_COMPOSE_CMD_DEV=docker-compose -p $(DOCKER_COMPOSE_PROJECT) -f $(DOCKER_COMPOSE_FILE_DEV)

PYTHON_EXEC=/usr/local/bin/python


run:
	$(DOCKER_COMPOSE_CMD_DEV) up --force-recreate --build -d

makemigrations:
	$(DOCKER_COMPOSE_CMD_DEV) exec wordle_bot alembic revision --autogenerate

alembic_init:
	$(DOCKER_COMPOSE_CMD_DEV) exec wordle_bot alembic init migrations

migrate:
	$(DOCKER_COMPOSE_CMD_DEV) exec wordle_bot alembic upgrade head

words2table:
	$(DOCKER_COMPOSE_CMD_DEV) exec wordle_api $(PYTHON_EXEC) words2table.py

check:
	@pre-commit run --all-files
