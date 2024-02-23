from sqlalchemy.ext.asyncio import AsyncSession

from models import Users


async def insert_user(session: AsyncSession, user_instance: Users) -> None:
    user = await session.get(Users, user_instance.id)
    if user is None:
        session.add(user_instance)
        await session.commit()
