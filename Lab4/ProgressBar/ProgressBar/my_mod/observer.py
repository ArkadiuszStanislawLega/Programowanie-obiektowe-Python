from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def unpack(self):
        pass
