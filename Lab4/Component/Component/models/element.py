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

    @property
    def name(self):
        return self._name

    @property
    def producent_name(self):
        return self._producent_name

    def __str__(self):
        return f'{type(self).__name__} - {self._id} - {self._producent_name} - {self._name}, cena: {self._price}zł'
