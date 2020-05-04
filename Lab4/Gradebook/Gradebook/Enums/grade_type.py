from enum import Enum


class GradeType(Enum):
    """
    Model ocen które można przydzielić uczniom.
    Arguments:
        Enum {[type]} -- Oceny uczni o bardzo dobrej do niedostatecznej w skali od 1 do 5
    """
    bdb = 5
    # dobry
    db = 4
    # dostateczny
    dst = 3
    # dopuszczający
    dop = 2
    # niedostateczny
    ndst = 1
