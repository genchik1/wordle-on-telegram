from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from models import UserWords
from querysets.words import get_today_word_qs, set_today_word_qs, check_word_qs, get_user_word_m2m_qs, add_word_qs


async def _create_today_word(session: AsyncSession) -> None:
    await session.execute(set_today_word_qs())
    await session.commit()


async def get_today_word_method(session: AsyncSession) -> str:
    smtm = await session.execute(get_today_word_qs())
    word = smtm.scalar_one_or_none()
    if not word:
        await _create_today_word(session)
        smtm = await session.execute(get_today_word_qs())
        word = smtm.scalar_one_or_none()
    return word.word


async def check_word_method(session: AsyncSession, word: str) -> bool:
    smtm = await session.execute(check_word_qs(word))
    word = smtm.scalar_one_or_none()
    if not word:
        return False
    return True


async def save_word(session: AsyncSession, user_id: int, word: str, is_guessed: bool) -> None:
    smtm = await session.execute(get_user_word_m2m_qs(user_id))
    instance = smtm.scalar_one_or_none()
    if instance is None:
        m2m = UserWords(user_id=user_id, day=datetime.now(), is_guessed=is_guessed, words=[word])
        session.add(m2m)
    else:
        instance.words.append(word)
        await session.execute(add_word_qs(instance.id, instance.words, is_guessed))
    await session.commit()
