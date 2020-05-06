from Enums.grade_type import GradeType
from Models.basic_model import BasicModel
from Models.student import Student
from Models.grade import Grade


class SchoolClass(BasicModel):
    def __init__(self):
        super().__init__()
        self.__id = 0
        self.__name = ""
        self.__students = {}

    # region Properties
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def students(self):
        return self.__students

    @property
    def average_grade(self):
        sum_counter = 0
        number_of_students = len(self.__students)
        if number_of_students > 0:
            for student in self.__students.values():
                sum_counter += student.average_grade
            return sum_counter/number_of_students
        else:
            return sum_counter

    def __str__(self):
        return f'{self.__id} {self.__name}'

    def print_list_of_students(self):
        print(*self.__students.values(), sep='\n')

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.__students.update({student.id: student})

    def remove_student(self, student_id):
        if isinstance(student_id, int) and student_id > 0:
            self.__students.pop(student_id)

    def modify(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():

                if key == "name":
                    self.__name = value
                    self.notify(name=self.__name)

                elif key == "add_student":
                    self.add_student(value)
                    self.notify(add_student=value)
        pass

    def notify(self, *args, **kwargs):
        if len(kwargs) > 0:
            self._obs_list.get("SchoolClassView").update(**kwargs)
        pass
