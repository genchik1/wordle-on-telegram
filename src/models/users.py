from __future__ import annotations

import typing

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import Mapped, relationship

from models._absctract import UserBase

from models.user_word_m2m import user_word_m2m

if typing.TYPE_CHECKING:
    from models import Words


class Users(UserBase):
    """Схема таблицы в базе данных хранящее список юзеров и их персональные настройки и ограничения"""

    utm = Column(String, default=None, nullable=True, doc='UTM метка, чтобы знать от куда пришел юзер')
    allows_write_to_pm = Column(Boolean, default=True, doc='Разрешил ли юзер отправку ему сообщений?')
    is_admin = Column(Boolean, default=False, doc='Является ли юзер админом (для кнопок в боте)')

    words: Mapped[set[Words]] = relationship(back_populates='users', secondary=user_word_m2m)

    def __str__(self) -> str:
        return self.username
