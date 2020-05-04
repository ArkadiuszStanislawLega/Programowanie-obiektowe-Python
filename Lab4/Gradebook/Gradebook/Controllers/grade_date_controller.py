from Controllers.controller import Controller
import datetime


class GradeDateController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        obj = input(
            'Żeby zaktualizować datę wciśnij "T". Żeby anulować wciśnij "N". ')
        print(80*"=")
        if obj == 'n':
            return False
        elif obj == 't':
            self._model.modify({"date": datetime.datetime.now()})
        else:
            print("Błędna wartość.")

        return True
