from sqlalchemy.ext.asyncio import AsyncSession

from models import Users
from querysets.users import get_admin_qs, get_users_qs, get_count_users_qs


async def insert_user(session: AsyncSession, user_instance: Users) -> None:
    """Добавление нового пользователя, если его еще нет в нашей системе."""
    user = await session.get(Users, user_instance.id)
    if user is None:
        session.add(user_instance)
        await session.commit()


async def is_admin(session: AsyncSession, user_id: int) -> bool:
    """Проверяем, является ли юзер администратором."""
    smtm = await session.execute(get_admin_qs(user_id))
    user = smtm.scalar_one_or_none()
    if user is None:
        return False
    return True


async def get_users(session: AsyncSession) -> list:
    """Получить список всех юзеров"""
    smtm = await session.execute(get_users_qs())
    return smtm.scalars().all()


async def get_count_users(session: AsyncSession):
    """Получить кол-во юзеров"""
    smtm = await session.execute(get_count_users_qs())
    return smtm.scalar()
