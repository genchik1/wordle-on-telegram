from __future__ import annotations

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from methods.words import get_today_word_method, check_word_method, save_word
from querysets.words import get_user_word_m2m_qs
from settings.db import get_async_session

words_router = APIRouter(prefix='/api/words', tags=['API'])


@words_router.get('/today', summary='Получение сегодняшнего слова')
async def get_today_word(
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> str:
    return await get_today_word_method(session)


@words_router.get(
    '/check',
    summary='Проверяем существует ли такое слово и сохраняем все существующие введенные слова.',
)
async def check_word(
    word: str,
    user_id: int,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> bool:
    is_exists = await check_word_method(session, word)
    if is_exists:
        background_tasks.add_task(save_word, session, user_id, word, word == await get_today_word_method(session))
    return is_exists


@words_router.get('/user', summary='Получаем список угаданных юзером слов.')
async def get_user_words(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),  # noqa: B008
) -> dict:
    smtm = await session.execute(get_user_word_m2m_qs(user_id))
    instance = smtm.scalar_one_or_none()
    result: dict = {'is_guessed': instance.is_guessed, 'words': {}}
    for index in range(1, 7):
        result['words'][index] = []
        if instance is not None:
            try:
                result['words'][index] = instance.words[index - 1]
            except IndexError:
                pass
    return result
