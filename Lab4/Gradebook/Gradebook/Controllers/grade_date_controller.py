from Controllers.controller import Controller
from Enums.grade_properties_type import GradePropertiesType
import datetime


class GradeDateController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        user_input = input(
            'Żeby zaktualizować datę wciśnij "T". Żeby anulować wciśnij "N". ')
        print(80*"=")
        if user_input.lower() == 'n':
            return False
        elif user_input.lower() == 't':
            self._model.modify(date=datetime.datetime.now())
        else:
            print("Błędna wartość.")

        return True
