from sqlalchemy import select, func, update
from sqlalchemy.orm import load_only
from datetime import datetime
from models import Words, UserWords


def get_today_word_qs() -> select:
    """Формирование запроса в базу данных для получения сегодняшнего слова"""
    return select(Words).options(load_only(Words.word)).where(Words.is_today == True)


def set_today_word_qs() -> tuple:
    """Получить случайное неиспользованное слово"""
    word = select(Words).options(load_only(Words.word))
    return (
        update(Words)
        .where(Words.word == word.where(Words.is_used == False).order_by(func.random()).first())
        .values(Words.is_today == True),
    )


def check_word_qs(word: str) -> select:
    """Проверяем есть ли такое слово в базе"""
    return select(Words).options(load_only(Words.id)).where(Words.word == word)


def get_user_word_m2m_qs(user_id: int) -> select:
    return select(UserWords).where(UserWords.user_id == user_id).where(UserWords.day == datetime.now().date())


def add_word_qs(instance_id: int, words: list[str], is_guessed: bool) -> select:
    return update(UserWords).where(UserWords.id == instance_id).values({'is_guessed': is_guessed, 'words': words})
