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

        options = ["Anuluj", "Zmień nazwę", "Zmień ocenę", "Zmień datę"]

        for i, value in enumerate(options):
            print(f'{i}. {value}')

        user_input = int(input("Wybierz opcję: "))
        if user_input > 0:
            if user_input == 1:
                self.update_name()

            elif user_input == 2:
                self.update_grade()

            elif user_input == 3:
                self.update_date()

    def update_name(self):
        self.__grade_name_controller.get_user_input()

    def update_grade(self):
        self.__grade_grade_controller.get_user_input()

    def update_date(self):
        self.__grade_date_controller.get_user_input()

    def get_user_input(self):
        pass
