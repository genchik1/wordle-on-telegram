from __future__ import annotations

from aiogram.fsm.state import State


class BotState(State):
    """
    State object
    """

    def __init__(self, state: str | None = None, group_name: str | None = None, text: str = '') -> None:
        super().__init__(state, group_name)
        self.text = text
