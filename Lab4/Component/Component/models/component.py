from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self):
        self._id = ""
        self._name = ""
        self._price = 0
        self._elements = []

    @property
    def price(self):
        if len(self._elements) > 0:
            current_price = self._price
            for element in self._elements:
                current_price += element.price
                return current_price
        else:
            return self._price

    @abstractmethod
    def add_element(self, element):
        pass

    @abstractmethod
    def remove_element(self, element):
        pass

    def __str__(self):
        value = ""
        if len(self._elements) > 0:
            for element in self._elements:
                value += f'{element._id} - {element._producent_name} - {element._name} cena: {element._price}\n'
            value += f'{self._id} {self._name} - {self.price}'
            return value

        return f'{self._id} {self._name} - {self.price}'
