from sqlalchemy import select
from models import Users


def get_admin_qs(user_id: int) -> select:
    """Формирование запроса в базу данных для получения юзера, если он является администратором."""
    return select(Users.id).where(Users.id == user_id, Users.is_admin == True)


def get_users_qs() -> select:
    """Список юзеров"""
    return select(Users)
