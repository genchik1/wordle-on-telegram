from __future__ import annotations
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from commands import AdminCommand
from methods.users import is_admin
from utils.keyboards import keyboard_builder, inline_builder

admin_router = Router()


@admin_router.message(Command(AdminCommand.admin_start.command))
async def admin_start(message: Message, session: AsyncSession, state: FSMContext) -> None:
    """Старт админа"""
    await state.clear()
    user_id = message.from_user.id
    if await is_admin(session=session, user_id=user_id):
        await message.answer(
            text='Вы в панели администратора',
            reply_markup=keyboard_builder([AdminCommand.admin_menu.name]),
            parse_mode='Markdown',
        )
    else:
        await message.answer(text=f'Вы не являетесь администратором!\nВаш id: {user_id}', parse_mode='Markdown')


@admin_router.message(F.text.in_(AdminCommand.admin_menu.commands))
async def admin_menu(message: Message, session: AsyncSession, state: FSMContext) -> None:
    await state.clear()
    user_id = message.from_user.id
    if await is_admin(session=session, user_id=user_id):
        text = 'Вам доступно следующее:\n\n- Отправка сообщения всем пользователям\n- Просмотр статистики'
        keyboard = [
            {
                'text': elem.name,
                'callback_data': elem.callback,
            }
            for elem in [
                AdminCommand.send_message,
                AdminCommand.statistic,
            ]
        ]
        await message.answer(text=text, reply_markup=inline_builder(keyboard), parse_mode='Markdown')
    else:
        await message.answer(text=f'Вы не являетесь администратором!\nВаш id: {user_id}', parse_mode='Markdown')
