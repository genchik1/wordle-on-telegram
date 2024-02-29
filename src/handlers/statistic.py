from __future__ import annotations

from aiogram import F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from commands import AdminCommand
from methods.users import get_count_users
from methods.words import get_today_word_method

statistic_router = Router()


@statistic_router.callback_query(F.data == AdminCommand.statistic.callback)
async def statistic(callback: CallbackQuery, session: AsyncSession) -> None:
    count_users = await get_count_users(session=session)
    today_word = await get_today_word_method(session=session)
    msg = f'Слово дня: {today_word}\n' f'Общее количество юзеров: {count_users}'
    await callback.message.answer(text=msg, parse_mode='html')
