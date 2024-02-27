from __future__ import annotations

from aiogram import Bot, F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from commands import AdminCommand
from methods.users import get_users
from utils.general_state import BotState
from utils.keyboards import inline_builder, inline_url_builder

send_message_router = Router()


class MessageCallbackFactory(CallbackData, prefix='create_message'):  # type: ignore
    action: str | None = None


class MessageForm(StatesGroup):
    message = BotState(text='Введите сообщение:')
    photo = BotState(text='Отправьте изображение:')
    url_name = BotState(text='Введите название ссылки:')
    url = BotState(text='Введите url ссылку:')


@send_message_router.callback_query(F.data == AdminCommand.send_message.callback)
async def new_message(callback: CallbackQuery, state: FSMContext) -> None:
    """Создание сообщения"""
    await state.clear()
    await state.set_state(MessageForm.message)
    keyboard = [{'text': 'Отмена', 'callback_data': MessageCallbackFactory(action='cancel').pack()}]
    await callback.message.edit_text(MessageForm.message.text, reply_markup=inline_builder(keyboard))


@send_message_router.message(MessageForm.message)
async def get_message(message: Message, state: FSMContext) -> None:
    """Отлавливание текста сообщения, переход на ссылку или пропуск ссылки"""
    await state.update_data(message=message.text)
    await state.set_state(MessageForm.url)
    keyboard = [{'text': 'Пропустить', 'callback_data': MessageCallbackFactory(action='url_skip').pack()}]
    await message.answer(MessageForm.url.text, reply_markup=inline_builder(keyboard))


@send_message_router.callback_query(MessageCallbackFactory.filter(F.action == 'url_skip'))
async def skip_url(callback: CallbackQuery, state: FSMContext) -> None:
    """Отлавливание пропуска ссылки, переход на фото"""
    await state.update_data()
    await state.set_state(MessageForm.photo)
    keyboard = [{'text': 'Пропустить', 'callback_data': MessageCallbackFactory(action='photo_skip').pack()}]
    await callback.message.edit_text(text=MessageForm.photo.text, reply_markup=inline_builder(keyboard))


@send_message_router.message(MessageForm.url)
async def get_url(message: Message, state: FSMContext) -> None:
    """Отлавливание ссылки если она введена (не нажато "Пропустить"), переход на название кнопки"""
    await state.update_data(url=message.text)
    await state.set_state(MessageForm.url_name)
    await message.answer(MessageForm.url_name.text)


@send_message_router.message(MessageForm.url_name)
async def get_photo(message: Message | CallbackQuery, state: FSMContext) -> None:
    """Отлавливание названия ссылки, переход на фото"""
    await state.update_data(url_name=message.text)
    await state.set_state(MessageForm.photo)
    keyboard = [{'text': 'Пропустить', 'callback_data': MessageCallbackFactory(action='photo_skip').pack()}]
    await message.answer(text=MessageForm.photo.text, reply_markup=inline_builder(keyboard))


@send_message_router.callback_query(MessageCallbackFactory.filter(F.action == 'photo_skip'))
async def without_photo(callback: CallbackQuery, state: FSMContext) -> None:
    """Показ и дальнейшие действия с сообщением без фото"""
    await state.update_data()
    data = await state.get_data()
    if 'url' in data.keys():  # показ сообщения с url кнопкой
        keyboard = [
            {
                'text': data['url_name'],
                'url': data['url'],
            }
        ]
        await callback.message.answer(
            text=data['message'], reply_markup=inline_url_builder(keyboard), parse_mode='Markdown'
        )
    else:  # показ простого сообщения
        await callback.message.answer(text=data['message'], parse_mode='Markdown')

    keyboard = [
        {'text': 'Отправить', 'callback_data': MessageCallbackFactory(action='confirm').pack()},
        {'text': 'Отмена', 'callback_data': MessageCallbackFactory(action='cancel').pack()},
    ]
    await callback.message.answer(
        text='Сообщение сформировано', reply_markup=inline_builder(keyboard), parse_mode='Markdown'
    )


@send_message_router.message(MessageForm.photo)
async def send_options(message: Message, state: FSMContext) -> None:
    """Показ и дальнейшие действия с сообщением с фото"""
    if message.photo:  # проверка на то что было отправлено именно фото
        await state.update_data(photo=message.photo[-1].file_id)  # сохраняем id фото
        data = await state.get_data()
        if 'url' in data.keys():
            keyboard = [
                {
                    'text': data['url_name'],
                    'url': data['url'],
                }
            ]
            await message.answer_photo(
                photo=data['photo'], caption=data['message'], reply_markup=inline_url_builder(keyboard)
            )
        else:
            await message.answer_photo(photo=data['photo'], caption=data['message'])
        confirm_message = 'Сообщение сформировано'
        keyboard = [
            {'text': 'Отправить', 'callback_data': MessageCallbackFactory(action='confirm').pack()},
            {'text': 'Отмена', 'callback_data': MessageCallbackFactory(action='cancel').pack()},
        ]

        await message.answer(text=confirm_message, reply_markup=inline_builder(keyboard))
    else:
        keyboard = [{'text': 'Пропустить', 'callback_data': MessageCallbackFactory(action='photo_skip').pack()}]
        await message.answer(text=MessageForm.photo.text, reply_markup=inline_builder(keyboard))


async def _send(bot: Bot, data: dict, user_id: int) -> None:
    if 'url' in data:
        keyboard = [
            {
                'text': data['url_name'],
                'url': data['url'],
            }
        ]
        if 'photo' in data.keys():
            await bot.send_photo(
                chat_id=user_id,
                photo=data['photo'],
                caption=data['message'],
                reply_markup=inline_url_builder(keyboard),
                parse_mode='Markdown',
            )
        else:
            await bot.send_photo(
                chat_id=user_id,
                photo=data['photo'],
                caption=data['message'],
                reply_markup=inline_url_builder(keyboard),
                parse_mode='Markdown',
            )
    elif 'photo' in data.keys():
        await bot.send_photo(chat_id=user_id, photo=data['photo'], caption=data['message'], parse_mode='Markdown')
    else:
        await bot.send_message(chat_id=user_id, text=data['message'], parse_mode='Markdown')


@send_message_router.callback_query(MessageCallbackFactory.filter(F.action == 'confirm'))
async def send(callback: CallbackQuery, session: AsyncSession, state: FSMContext, bot: Bot) -> None:
    """Рассылка сообщения"""
    users_list = await get_users(session=session)
    data = await state.get_data()
    await state.clear()

    for user in users_list:
        await _send(bot, data, user.id)
    await callback.message.answer('Сообщение было отправлено пользователям')


@send_message_router.callback_query(MessageCallbackFactory.filter(F.action == 'cancel'))
async def cancel(callback: CallbackQuery, state: FSMContext) -> None:
    """Отмена отправки сообщения"""
    await state.clear()
    await callback.message.edit_text('Отправка отменена')
