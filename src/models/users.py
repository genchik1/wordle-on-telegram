from __future__ import annotations

import typing

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import Mapped, relationship

from models._absctract import UserBase

if typing.TYPE_CHECKING:
    from models import UserWords


class Users(UserBase):
    """Схема таблицы в базе данных хранящее список юзеров и их персональные настройки и ограничения"""

    utm = Column(String, default=None, nullable=True, doc='UTM метка, чтобы знать от куда пришел юзер')
    allows_write_to_pm = Column(Boolean, default=True, doc='Разрешил ли юзер отправку ему сообщений?')
    is_admin = Column(Boolean, default=False, doc='Является ли юзер админом (для кнопок в боте)')

    words: Mapped[list[UserWords]] = relationship(back_populates='user')

    def __str__(self) -> str:
        return self.username
