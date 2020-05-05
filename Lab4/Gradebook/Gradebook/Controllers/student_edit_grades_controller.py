from Controllers.controller import Controller
from Controllers.grade_controller import GradeController
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
            seleceted_grade = self._model.grades.get(keys[grade_user_select])
            GradeController(model=seleceted_grade,
                            view=seleceted_grade.obs_list.get("GradeView"))

        except(ValueError):
            print("Błędna wartość.")
