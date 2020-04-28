from my_mod.observer import Observer
import time
import random


class Package(Observer):

    def __init__(self, id):
        super().__init__()
        self.__id = id
        self.__status = False

    @property
    def status(self):
        return self.__status

    @property
    def id(self):
        return self.__id

    def unpack(self):
        if not self.__status:
            random_second = random.uniform(0, 2)
            time.sleep(random_second)
            self.__status = True
