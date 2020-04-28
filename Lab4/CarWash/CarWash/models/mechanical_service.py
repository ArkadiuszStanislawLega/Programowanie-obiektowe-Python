from models.service import Service
from abc import ABC, abstractmethod


class MechanicalService(ABC, Service):
    def __init__(self):
        super().__init__()
        self._name = "Mechaniczna usługa"

    def clean(self):
        print('Stanowisko czyszczenia mechanicznego pojazdu jest dostępne.')

    def paid_for_service(self):
        if not self._is_paid:
            print(f'Płacę za {self._name}')
            self._is_paid = True
        else:
            print(f'Usługa {self._name} jest już opłacona.')
