import typing
from fastapi import Request
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend

from admin.users import UsersAdmin
from admin.words import WordsAdmin
from settings.base import AUTH_TOKEN
from utils.auth import check_auth, create_token, check_token


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        if check_auth(form['username'], form['password']):
            request.session.update({'token': create_token()})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return check_token(request.session.get('token'))


def init_admin_panel(app: typing.Any, engine: typing.Any) -> None:
    authentication_backend = AdminAuth(secret_key=AUTH_TOKEN)
    admin_views = Admin(
        app,
        engine,
        authentication_backend=authentication_backend,
        debug=False,
    )

    admin_views.add_view(UsersAdmin)
    admin_views.add_view(WordsAdmin)
