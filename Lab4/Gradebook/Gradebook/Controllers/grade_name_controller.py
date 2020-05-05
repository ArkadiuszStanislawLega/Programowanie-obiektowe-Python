from Controllers.controller import Controller
from Enums.grade_properties_type import GradePropertiesType


class GradeNameController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        user_input = input(
            'Podaj nową nazwę oceny: ')
        print(80*"=")
        self._model.modify(name=user_input)
