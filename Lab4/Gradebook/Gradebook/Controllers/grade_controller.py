from Controllers.controller import Controller
from Controllers.grade_date_controller import GradeDateController
from Controllers.grade_grade_controller import GradeGradeController
from Controllers.grade_name_controller import GradeNameController
import datetime


class GradeController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

        self.__grade_name_controller = GradeNameController(
            model=model, view=view)
        self.__grade_grade_controller = GradeGradeController(
            model=model, view=view)
        self.__grade_date_controller = GradeDateController(
            model=model, view=view)

    def update_name(self):
        self.__grade_name_controller.get_user_input()

    def update_grade(self):
        self.__grade_grade_controller.get_user_input()

    def update_date(self):
        self.__grade_date_controller.get_user_input()

    def get_user_input(self):
        pass
