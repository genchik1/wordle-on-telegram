from __future__ import annotations

import typing

from sqlalchemy import ForeignKey, Column, Boolean, Index, BigInteger, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from models._absctract import DatetimeBaseMixin
from settings.db import Base

if typing.TYPE_CHECKING:
    from models import Users


class UserWords(DatetimeBaseMixin, Base):
    """Ассоциативная таблица для связи угаданных юзером слов."""

    __tablename__ = 'user_words'

    id = Column(BigInteger, primary_key=True)  # noqa: A003 VNE003
    user_id = Column('user_id', ForeignKey('users.id'))
    user: Mapped[Users] = relationship(back_populates='words')
    is_guessed = Column(Boolean, doc='Угадал ли слово дня?')
    today_word = Column(String)
    words = Column(JSONB)

    user_today_idx = Index('user_today_word_idx', 'user_id', 'today_word', unique=True)
