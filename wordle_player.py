from abc import ABC, abstractmethod


class WordlePlayer(ABC):
    def __init__(self, words) -> None:
        super().__init__(words)
    @abstractmethod
    def guess(self):
        pass
    @abstractmethod
    def cb(self, resp):
        pass