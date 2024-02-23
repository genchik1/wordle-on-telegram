from sqladmin import ModelView

from models import Users


class UsersAdmin(ModelView, model=Users):  # type: ignore
    name_plural = 'users'
    name = 'users'
    icon = 'fa-solid fa-person'
    column_list = [
        Users.id,
        Users.username,
        Users.utm,
        Users.is_admin,
    ]
    page_size = 25
    page_size_options = [50, 100]
