from sqladmin import ModelView

from models import Words


class WordsAdmin(ModelView, model=Words):  # type: ignore
    name_plural = 'words'
    name = 'words'
    icon = 'fa-solid fa-file-word'
    column_list = [
        Words.word,
        Words.is_today,
        Words.is_used,
    ]
    page_size = 25
    page_size_options = [50, 100]
    column_sortable_list = [Words.is_today, Words.is_used]
