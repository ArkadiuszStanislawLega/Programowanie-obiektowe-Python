from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self):
        self._id = ""
        self._producent_name = ""
        self._name = ""
        self._price = 0

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f'{self._id} - {self._producent_name} - {self._name} cena: {self._price}'
