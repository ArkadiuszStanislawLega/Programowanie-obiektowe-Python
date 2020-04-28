import progressbar
import time
from my_mod.file import File
from my_mod.package import Package

# Ilość paczek z których składa się plik.
NUMBER_OF_PACKAGES = 15


def main():

    file = File(NUMBER_OF_PACKAGES)
    for i in range(NUMBER_OF_PACKAGES):
        file.add_package(Package(i))

    print("Rozpakowuje plik:")
    file.unpack_packages()


if '__main__' == __name__:
    main()
