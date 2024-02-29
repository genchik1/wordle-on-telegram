import asyncio

import schedule
import time

from methods.words import create_today_word
from settings.db import async_session


async def task():
    async with async_session() as session:
        try:
            await create_today_word(session)
        finally:
            await session.close()


def main():
    asyncio.run(task())


schedule.every().day.at('9:00', 'Europe/Moscow').do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
