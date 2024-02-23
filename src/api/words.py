from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from methods.words import get_today_word_method
from settings.db import get_async_session

words_router = APIRouter()


@words_router.get('/api/words/today', tags=['API'], summary='Получение сегодняшнего слова')
async def get_today_word(
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> str:
    return await get_today_word_method(session)
