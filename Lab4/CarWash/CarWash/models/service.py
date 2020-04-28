from abc import ABC, abstractmethod


class Service:
    def __init__(self):
        self._name = ""
        self._price = 0
        self._is_paid = False

    @abstractmethod
    def clean(self):
        pass

    @abstractmethod
    def paid_for_service(self):
        pass

    @property
    def name(self):
        return self._name
