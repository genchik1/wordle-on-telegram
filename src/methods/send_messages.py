from __future__ import annotations

import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from methods.users import get_users
from settings.base import BOT_TOKEN

api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'


async def send_message_for_all_users(
    session: AsyncSession,
    text: str,
) -> None:
    users_ids = {user.id for user in await get_users(session=session)}
    async with aiohttp.ClientSession() as session:
        for user_id in users_ids:
            try:
                await session.post(url=api_url, json={'chat_id': user_id, 'text': text, 'parse_mode': 'Markdown'})
            except:  # noqa: E722
                # тут мы ставим защиту, на случай, если юзер не отказался от уведомлений, упадет ошибка
                pass
