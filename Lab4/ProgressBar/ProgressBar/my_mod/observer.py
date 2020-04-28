from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class FirstObserver(Observer):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        print('First observer')
        if args:
            print(args)

        if kwargs:
            print(kwargs)
