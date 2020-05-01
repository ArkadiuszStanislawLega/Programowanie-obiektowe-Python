from Models.grade_type import GradeType
import datetime


class Grade:
    def __init__(self):
        # id ucznia składa się z jego numeru id oraz daty wystawienia oceny.
        self.__id = ""
        self.__name = ""
        self.__grade = GradeType.ndst
        self.__date = datetime.datetime.now()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, str):
            self.__id = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value: GradeType):
        if isinstance(value, GradeType):
            self.__grade = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return f'{self.__id}. {self.__name} - {self.__grade}'
