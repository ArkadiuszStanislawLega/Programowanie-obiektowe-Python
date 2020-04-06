from .person import Person
from .medical_specialization import MedicalSpecialization


class Doctor(Person):
    def __init__(self):
        self.__medical_specialization = MedicalSpecialization.doctor
