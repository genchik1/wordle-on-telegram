import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from handlers.admin import admin_router
from handlers.send_message import send_message_router
from handlers.start import start_router
from handlers.statistic import statistic_router
from middlewares.session import DbSessionMiddleware
from settings.base import BOT_TOKEN
from settings.db import engine, Base, async_session


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.MARKDOWN_V2)

    dp = Dispatcher()
    dp.include_routers(start_router, admin_router, send_message_router, statistic_router)

    dp.update.middleware(DbSessionMiddleware(session_pool=async_session))
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
