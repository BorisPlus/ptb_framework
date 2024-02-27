from abc import (
    ABC,
    abstractmethod
)

from config import Config


class DialogueBotInterface(ABC):
    config: Config
    dialogs = dict()
    operations_count = 0

    @abstractmethod
    def __init__(self, config: Config):
        pass
