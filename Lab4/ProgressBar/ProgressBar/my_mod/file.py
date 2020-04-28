import time
import progressbar
from my_mod.package import Package


class File:
    def __init__(self, max_value):
        self.__max_value = max_value
        self.__packages = []

    def add_package(self, package: Package):
        if len(self.__packages) < self.__max_value:
            self.__packages.append(package)

    def unpack_packages(self):
        for package in progressbar.progressbar(self.__packages):
            package.unpack()

            if not package.status:
                print(f'\nWystąpił błąd w paczce {package.id}.')
                break
