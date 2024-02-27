from dataclasses import dataclass

from utils import CommandBase


@dataclass
class AdminCommand:
    admin_start = CommandBase(name='Панель администратора', command='admin')
    admin_menu = CommandBase(name='Меню', command='/admin_menu')
    send_message = CommandBase(name='Отправить сообщение', callback='send_message_callback')
    statistic = CommandBase(name='Статистика', callback='statistic')


class BotCommand:
    start = CommandBase(command='start')
