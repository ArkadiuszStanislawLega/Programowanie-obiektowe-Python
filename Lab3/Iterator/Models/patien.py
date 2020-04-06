from .person import Person
from .patient_type import PatientType


class Patient(Person):
    def __init__(self):
        self.__patient_type = PatientType.normal
