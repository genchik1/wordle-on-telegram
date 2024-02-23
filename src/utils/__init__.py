from dataclasses import dataclass


@dataclass
class CommandBase:
    def __init__(self, name: str = '', command: str = '', callback: str = ''):
        self.name: str = name
        self.command: str = command
        self.callback: str = callback

    @property
    def commands(self) -> tuple:
        return self.name, self.command
