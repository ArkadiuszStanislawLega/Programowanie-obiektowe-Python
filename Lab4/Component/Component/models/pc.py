from models.component import Component
from models.element import Element


class Pc(Component):
    def __init__(self):
        super().__init__()

    def add_element(self, element: Element):
        if isinstance(element, Element):
            self._elements.append(element)

    def remove_element(self, element: Element):
        if isinstance(element, Element):
            self._elements.remove(element)
