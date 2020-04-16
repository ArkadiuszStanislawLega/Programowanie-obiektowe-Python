from abc import ABC, abstractmethod


class Modification:

    @abstractmethod
    def action(self, picture):
        pass
