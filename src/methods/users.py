from sqlalchemy.ext.asyncio import AsyncSession

from models import Users


async def insert_user(session: AsyncSession, user_instance: Users) -> None:
    """Добавление нового пользователя, если его еще нет в нашей системе."""
    user = await session.get(Users, user_instance.id)
    if user is None:
        session.add(user_instance)
        await session.commit()
