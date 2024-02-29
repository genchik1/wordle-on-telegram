import asyncio

import schedule
import time

from methods.send_messages import send_message_for_all_users
from methods.words import create_today_word
from settings.db import async_session


async def task():
    async with async_session() as session:
        try:
            await create_today_word(session)
            await send_message_for_all_users(session, text='"5 БУКВ" Новое слово уже ждет вас.')
        finally:
            await session.close()


def main():
    asyncio.run(task())


# schedule.every(1).minute.do(main)
schedule.every().day.at('11:00', 'Europe/Moscow').do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
