from __future__ import annotations

from aiogram import Router
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from sqlalchemy.ext.asyncio import AsyncSession

from commands import BotCommand
from methods.users import insert_user
from models import Users
from settings.base import WEBAPP_DOMAIN

start_router = Router()

START_MESSAGE = """🧩 Добро пожаловать в игру 5 букв (wordle). Проект с открытым кодом, был создан, чтобы быть шаблоном \
для быстрого создания сервисов в телеграм с использованием webapp. \


Новое слово каждый день в 11 утра по московскому времени.

Разработчик: [@keskiy](https://t.me/keskiy)
Код: [https://github.com/genchik1...](https://github.com/genchik1/wordle-on-telegram)
"""


def _get_keyboard() -> InlineKeyboardMarkup:
    """Кнопки в стартовом сообщении"""
    webapp_catalog = WebAppInfo(url=WEBAPP_DOMAIN)
    keyboard = [[InlineKeyboardButton(text='Играть', web_app=webapp_catalog)]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


@start_router.message(CommandStart(deep_link=True))
@start_router.message(Command(BotCommand.start.command))
async def start_command(message: Message, command: CommandObject, session: AsyncSession) -> None:
    await insert_user(session, Users(id=message.from_user.id, username=message.from_user.username, utm=command.args))

    await message.answer(
        START_MESSAGE, reply_markup=_get_keyboard(), parse_mode='Markdown', disable_web_page_preview=True
    )
