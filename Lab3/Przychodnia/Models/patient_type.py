from enum import Enum


class PatientType(Enum):
    """
    Klasyfikacja rodzajów pacjentów.
    """
    # normalny
    normal = 1
    # pilny
    urgent = 2
