from Controllers.controller import Controller
from Models.grade import Grade
from Models.student import Student
from Views.grade_view import GradeView
from Enums.grade_type import GradeType
import datetime


class SchoolClassAddStudentController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        print(f'Dodawanie nowego ucznia do klasy: {self._model} ')
        print(80*"=")
        user_input_new_student_name = input("Podaj imię ucznia: ")
        user_input_new_student_surname = input("Podaj nazwisko ucznia: ")

        new_student = Student()
        new_student.id = len(self._model.students)+1
        new_student.name = user_input_new_student_name
        new_student.surname = user_input_new_student_surname
        self._model.modify(add_student=new_student)
        print(80*"=")
