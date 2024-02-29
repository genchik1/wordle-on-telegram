from __future__ import annotations

import datetime
import uuid

from sqlalchemy import BigInteger, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import DateTime

from settings.db import Base


class UUIDBaseMixin:
    id = Column(  # noqa: A003 VNE003
        UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4
    )


class DatetimeBaseMixin(Base):
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    __abstract__ = True


class UserBase(DatetimeBaseMixin, Base):
    """Схема таблицы в базе данных хранящее список юзеров"""

    id = Column(  # noqa: A003 VNE003
        BigInteger, nullable=False, primary_key=True, doc='Первичный ключ и id пользователя телеграм'
    )
    username = Column(String, nullable=False, unique=True, doc='Имя пользователя телеграм')

    __tablename__ = 'users'
    __abstract__ = True
