from sqlalchemy import select, func, update
from sqlalchemy.orm import load_only

from models import Words


def get_today_word_qs() -> select:
    """Формирование запроса в базу данных для получения сегодняшнего слова"""
    return select(Words).options(load_only(Words.word)).where(Words.is_today == True)


def set_today_word_qs() -> tuple:
    """Получить случайное неиспользованное слово"""
    word = select(Words).options(load_only(Words.word))
    return (
        update(Words).where(Words.word in word.where(Words.is_today == True)).values(Words.is_today == True),
        update(Words)
        .where(Words.word == word.where(Words.is_used == False).order_by(func.random()).first())
        .values(Words.is_today == True),
    )
