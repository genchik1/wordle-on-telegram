import hashlib
from datetime import datetime, timedelta

import jwt

from settings.base import AUTH_USERNAME, HASH_PASSWORD, AUTH_SALT, AUTH_TOKEN, ALGORITHM


def check_auth(username: str, password: str) -> bool:
    """Валидация входа в панель администратора"""
    if username == AUTH_USERNAME:
        if HASH_PASSWORD == hashlib.md5((password + AUTH_SALT).encode()).hexdigest():
            return True
    return False


def create_token():
    return jwt.encode(
        {'exp': int((datetime.utcnow() + timedelta(days=1)).timestamp())}, AUTH_TOKEN, algorithm=ALGORITHM
    )


def check_token(token: str | None) -> bool:
    if not token:
        return False
    return jwt.decode(token, AUTH_TOKEN, algorithms=ALGORITHM).get('exp') > int((datetime.utcnow()).timestamp())
