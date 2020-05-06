from Controllers.controller import Controller
from Controllers.school_class_add_student_controller import SchoolClassAddStudentController
from Controllers.school_class_name_controller import SchoolClassNameController
from Controllers.student_controller import StudentController
from Views.student_view import StudentView
import datetime
import os


class SchoolClassController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

        self.__school_class_name_controller = SchoolClassNameController(
            model=model, view=view)
        self.__school_class_add_student_controller = SchoolClassAddStudentController(
            model=model, view=view)

        self.__is_exit = False

        options = ["Anuluj", "Zmień nazwę", "Dodaj ucznia",
                   "Wyświetl uczni", "Wyświetl średnią klasy", "Edytuj ucznia"]
        while not self.__is_exit:
            for i, value in enumerate(options):
                print(f'{i}. {value}')

            user_input = int(input("Wybierz opcję: "))
            os.system('cls')

            if user_input == 0:
                self.__is_exit = True
                print(80*"=")

            elif user_input == 1:
                self.update_name()

            elif user_input == 2:
                self.add_student()

            elif user_input == 3:
                self._model.print_list_of_students()
                print(80*"=")

            elif user_input == 4:
                print(f'Średnia klasy: {self._model.average_grade}')
                print(80*"=")

            elif user_input == 5:
                self.get_user_input()

    def update_name(self):
        self.__school_class_name_controller.get_user_input()

    def add_student(self):
        self.__school_class_add_student_controller.get_user_input()

    def get_user_input(self):
        keys = []
        for i, student in enumerate(self._model.students.values()):
            print(f'{i}. {student}')
            keys.append(student.id)

        user_input = int(input("Uczeń do edycji: "))
        student = self._model.students.get(keys[user_input])
        student_view = StudentView(model=student)
        student.add_observer(student_view)
        StudentController(model=student, view=student_view)
