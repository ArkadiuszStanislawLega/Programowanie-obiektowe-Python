from Controllers.controller import Controller
from Controllers.student_add_grade_controller import StudentAddGradeController
from Controllers.student_name_controller import StudentNameController
from Controllers.student_surname_controller import StudentSurnameController


class StudentController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

        self.__student_name_controller = StudentNameController(
            model=model, view=view)
        self.__student_surname_controller = StudentSurnameController(
            model=model, view=view)
        self.__student_add_grade_controller = StudentAddGradeController(
            model=model, view=view)

    def update_name(self):
        self.__student_name_controller.get_user_input()

    def update_surname(self):
        self.__student_surname_controller.get_user_input()

    def add_grade(self):
        self.__student_add_grade_controller.get_user_input()

    def get_user_input(self):
        pass
