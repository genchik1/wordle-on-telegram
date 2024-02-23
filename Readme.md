# 5 БУКВ (Wordle) в телеграм

Проект был создан, чтобы быть шаблоном для быстрого создания сервисов в телеграм с использованием webapp.

🧩 Игра: https://t.me/wordle_ru_game_bot


### Стек

- Backend
  - Python3.11 
  - Fastapi
  - Asyncpg + Sqlalchemy + Alembic
  - Sqladmin
  - Aiogram
- Frontend
  - React
  - Vite
- Docker

### Разработка

- Локальный запуск проекта `make run`
- Далее необходимо создать базу данных:
  - docker ps -- покажет запущенные контейнеры и их id
  - перейти в контейнер базы `docker exec -it <container_id> /bin/bash`
  - `psql -U postgres`
  - `create database worle_db;`
- Чтобы заполнить таблицу words выполните `make words2table`


- Установка python библиотек с помощью poetry `poetry add <lib>`
- Удаление `poetry remove <lib>`
- Проверить код чекерами и линтерами (ruff + mypy) `make check`


- HASH_PASSWORD - `echo -n <password><salt> | md5sum`
- SECRET_KEY - `openssl rand -hex 32`
