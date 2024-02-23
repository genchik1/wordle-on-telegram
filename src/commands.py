from dataclasses import dataclass

from utils import CommandBase


@dataclass
class AdminCommand:
    admin_start = CommandBase(name='Панель администратора', command='admin')
    admin_menu = CommandBase(name='Меню', command='/admin_menu')
    send_message = CommandBase(name='Отправить сообщение', callback='send_message_callback')
    to_web = CommandBase(name='Перейти в web', callback='to_web_callback')
    welcome_message = CommandBase(name='Приветственное сообщение', callback='welcome_message_callback')
    remove_deleted_users = CommandBase(name='Удалить отписавшихся пользователей', callback='remove_deleted_users')
    statistic = CommandBase(name='Статистика', callback='statistic')


class BotCommand:
    start = CommandBase(command='start')
