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
        current_price = 0
        counter = 1
        if len(self._elements) > 0:
            for element in self._elements:
                value += f'{counter}. {element}\n'
                current_price += element.price
                counter += 1
            value += f'{type(self).__name__} - cena: {current_price}zł'
            return value

        return f'{self._id} {self._name} - {self.price}'
