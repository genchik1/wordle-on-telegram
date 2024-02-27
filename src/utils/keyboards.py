from __future__ import annotations

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def keyboard_builder(keyboard: list) -> ReplyKeyboardMarkup:
    """Универсальный метод для вывода реплай кнопок."""
    builder = ReplyKeyboardBuilder()
    [builder.button(text=key) for key in keyboard]
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def inline_builder(data: list[dict]) -> InlineKeyboardMarkup:
    """Универсальный метод для вывода инлайн кнопок."""
    builder = InlineKeyboardBuilder()
    [builder.add(InlineKeyboardButton(text=dt['text'], callback_data=dt['callback_data'])) for dt in data]
    builder.adjust(2)
    return builder.as_markup()


def inline_url_builder(data: list[dict]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    [builder.add(InlineKeyboardButton(text=dt['text'], url=dt['url'])) for dt in data]
    builder.adjust(2)
    return builder.as_markup()
