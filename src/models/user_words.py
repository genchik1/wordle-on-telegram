from __future__ import annotations

import typing

from sqlalchemy import ForeignKey, Column, Boolean, Date, Index, BigInteger
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from settings.db import Base

if typing.TYPE_CHECKING:
    from models import Users


class UserWords(Base):
    """Ассоциативная таблица для связи угаданных юзером слов."""

    __tablename__ = 'user_words'

    id = Column(BigInteger, primary_key=True)  # noqa: A003 VNE003
    user_id = Column('user_id', ForeignKey('users.id'))
    user: Mapped[Users] = relationship(back_populates='words')
    is_guessed = Column(Boolean, doc='Угадал ли слово дня?')
    day = Column(Date)
    words = Column(JSONB)

    user_day_idx = Index('user_day_idx', 'user_id', 'day', unique=True)
