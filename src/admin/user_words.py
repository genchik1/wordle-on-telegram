from sqladmin import ModelView

from models import UserWords


class UserWordsAdmin(ModelView, model=UserWords):  # type: ignore
    name_plural = 'user_words'
    name = 'user_words'
    icon = 'fa-solid fa-pen'
    column_list = [
        UserWords.user,
        UserWords.today_word,
        UserWords.is_guessed,
        UserWords.created_at,
    ]
    page_size = 25
    page_size_options = [50, 100]
    column_sortable_list = [UserWords.created_at]
