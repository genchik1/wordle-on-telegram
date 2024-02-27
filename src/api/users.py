from __future__ import annotations

import typing

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from methods.users import insert_user
from models import Users
from schemas.users import UserSchema
from settings.db import get_async_session

users_router = APIRouter()


@users_router.post('/api/user', tags=['API'], summary='Создание нового юзера')
async def create_or_update_user(
    data: UserSchema,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> typing.Any:
    background_tasks.add_task(insert_user, session, Users(id=data.id, username=data.username, utm=data.utm))
