from sqlalchemy.ext.asyncio import AsyncSession

from querysets.words import get_today_word_qs, set_today_word_qs


async def _create_today_word(session: AsyncSession) -> None:
    with session.begin():
        for query in set_today_word_qs():
            await session.execute(query)
        await session.commit()


async def get_today_word_method(session: AsyncSession) -> str:
    smtm = await session.execute(get_today_word_qs())
    word = smtm.scalar_one_or_none()
    if not word:
        await _create_today_word(session)
        smtm = await session.execute(get_today_word_qs())
        word = smtm.scalar_one_or_none()
    return word.word
