from __future__ import annotations

from sqlalchemy import Column, String, Boolean

from models._absctract import UUIDBaseMixin, DatetimeBaseMixin
from settings.db import Base


class Words(UUIDBaseMixin, DatetimeBaseMixin, Base):
    """Схема таблицы в базе данных хранящее список слов"""

    __tablename__ = 'words'

    word = Column(String(5))
    is_used = Column(Boolean, default=False, doc='Было ли данное слово уже использовано?')
    is_today = Column(Boolean, default=False, doc='Сегодняшнее слово')

    def __str__(self) -> str:
        return self.word
