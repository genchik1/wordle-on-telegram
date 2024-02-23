from __future__ import annotations

from sqlalchemy import ForeignKey, Table, Column
from settings.db import Base


user_word_m2m = Table(
    'user_words_m2m',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('word_id', ForeignKey('words.id'), primary_key=True),
    comment='Ассоциативная таблица для связи угаданных юзером слов.',
)
