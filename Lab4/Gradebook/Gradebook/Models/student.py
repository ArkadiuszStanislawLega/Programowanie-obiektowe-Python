from Enums.grade_type import GradeType
from Models.basic_model import BasicModel
from Models.grade import Grade


class Student(BasicModel):
    def __init__(self):
        super().__init__()
        self.__id = 0
        self.__name = ""
        self.__surname = ""
        self.__grades = {}
    # region Properties
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def full_name(self):
        return f'{self.__name} {self.__surname}'

    @property
    def grades(self):
        return self.__grades

    @property
    def average_grade(self):
        sum_counter = 0
        number_of_grades = len(self.__grades)
        if number_of_grades > 0:
            for grade in self.__grades.values():
                sum_counter += grade.grade.value
            return sum_counter/number_of_grades
        else:
            return sum_counter

    # endregion

    def __str__(self):
        return f'{self.__name} {self.__surname}'

    def __repr__(self):
        return f'{self.__name} {self.__surname}'

    def add_grade(self, grade: Grade):
        if isinstance(grade, Grade):
            if grade.id is not self.__grades.keys():
                self.__grades[grade.id] = grade

    def remove_grade(self, grade: Grade):
        if isinstance(grade, Grade):
            self.__grades.pop(grade.id)

    def print_grades(self):
        for grade in self.__grades.values():
            print(f'{grade}')

    def modify(self, *args, **kwargs):
        pass
        # if len(kwargs) > 0:
        #     for key, value in kwargs.items():

        #         if key == "name":
        #             self.__name = value
        #             self.notify(name=self.__name)

        #         elif key == "grade":
        #             self.__grade = value
        #             self.notify(grade=self.__grade)

        #         elif key == "date":
        #             self.__date = value
        #             self.notify(date=self.__date)

    def notify(self, *args, **kwargs):
        pass
        # if len(kwargs) > 0:
        #     self._obs_list.get("GradeView").update(**kwargs)
