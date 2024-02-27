from sqlalchemy import select, func, update
from sqlalchemy.orm import load_only
from datetime import datetime
from models import Words, UserWords


def get_today_word_qs() -> select:
    """Формирование запроса в базу данных для получения сегодняшнего слова"""
    return select(Words.word).where(Words.is_today == True)


def set_today_word_qs() -> tuple:
    """Получить случайное неиспользованное слово и заменить слово дня"""
    return (
        update(Words)
        .where(Words.word == select(Words.word).where(Words.is_today == True))
        .values({Words.is_today: False}),
        update(Words)
        .where(Words.word == select(Words.word).where(Words.is_used == False).order_by(func.random()).limit(1))
        .values({Words.is_today: True, Words.is_used: True})
        .returning(Words.word),
    )


def check_word_qs(word: str) -> select:
    """Проверяем есть ли такое слово в базе"""
    return select(Words.id).where(Words.word == word)


def get_user_word_m2m_qs(user_id: int) -> select:
    """Получаем список введенных слов юзером за сегодня."""
    return select(UserWords).where(UserWords.user_id == user_id).where(UserWords.day == datetime.now().date())


def add_word_qs(instance_id: int, words: list[str], is_guessed: bool) -> select:
    """Добавляем введенное слово"""
    return update(UserWords).where(UserWords.id == instance_id).values({'is_guessed': is_guessed, 'words': words})
