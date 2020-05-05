from Enums.grade_type import GradeType
from Models.basic_model import BasicModel
import datetime


class Grade(BasicModel):
    def __init__(self):
        super().__init__()
        # id ucznia składa się z jego numeru id oraz daty wystawienia oceny.
        self.__id = ""
        self.__name = ""
        self.__grade = GradeType.ndst
        self.__date = datetime.datetime.now()
    # region Properties
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, str):
            self.__id = value
            self.modify()

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value: GradeType):
        if isinstance(value, GradeType):
            self.__grade = value
            self.modify()

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
    # endregion

    def __str__(self):
        return f'{self.__id}. {self.__name} - {self.__grade}'

    def modify(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():

                if key == "name":
                    self.__name = value
                    self.notify(name=self.__name)

                elif key == "grade":
                    self.__grade = value
                    self.notify(grade=self.__grade)

                elif key == "date":
                    self.__date = value
                    self.notify(date=self.__date)

    def notify(self, *args, **kwargs):
        if len(kwargs) > 0:
            self._obs_list.get("GradeView").update(kwargs)
