from __future__ import annotations

import typing

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship, Mapped

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base

from models.user_word_m2m import user_word_m2m

if typing.TYPE_CHECKING:
    from models import Users


class Words(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Схема таблицы в базе данных хранящее список слов"""

    __tablename__ = 'words'

    word = Column(String(5))
    is_used = Column(Boolean, default=False, doc='Было ли данное слово уже использовано?')
    is_today = Column(Boolean, default=False, doc='Сегодняшнее слово')

    users: Mapped[set[Users]] = relationship(back_populates='words', secondary=user_word_m2m)

    def __str__(self) -> str:
        return self.word
