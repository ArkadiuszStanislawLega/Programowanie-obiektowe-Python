from Controllers.controller import Controller
from Controllers.grade_grade_controller import GradeGradeController
from Controllers.grade_name_controller import GradeNameController
from Controllers.grade_date_controller import GradeDateController
from Views.grade_view import GradeView
from Enums.grade_type import GradeType


class StudentEditGradesController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        print(f'Edytowanie stopni ucznia: {self._model} ')
        print(80*"=")
        keys = []

        for i, value in enumerate(self._model.grades):
            keys.append(value)
            print(f'{i}. {self._model.grades.get(value)}')

        try:
            grade_user_select = int(input("Ocena którą chcesz edytować: "))
            print(80*"=")

            options = ["Anuluj", "Nazwa",  "Stopień", "Data"]

            for i, value in enumerate(options):
                print(f'{i}. {value}')

            option_user_select = int(input("Wybierz opcję: "))
            if option_user_select > 0:
                selected_grade = self._model.grades.get(
                    keys[grade_user_select])
                selected_grade_view = selected_grade.obs_list.get("GradeView")

                if option_user_select == 1:
                    grade_name_controler = GradeNameController(
                        view=selected_grade_view, model=selected_grade)
                    grade_name_controler.get_user_input()

                elif option_user_select == 2:
                    grade_grade_controler = GradeGradeController(
                        view=selected_grade_view, model=selected_grade)
                    grade_grade_controler.get_user_input()

                elif option_user_select == 3:
                    grade_date_controler = GradeDateController(
                        view=selected_grade_view, model=selected_grade)
                    grade_date_controler.get_user_input()
            elif option_user_select == 0:
                print(80*"=")

        except(ValueError):
            print("Błędna wartość.")
