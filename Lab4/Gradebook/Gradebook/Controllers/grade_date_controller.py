from Controllers.controller import Controller
import datetime


class GradeDateController(Controller):
    def __init__(self, view, model):
        super().__init__(view, model)

    def get_user_input(self):
        obj = input(
            'Żeby zaktualizować datę wciśnij "T". Żeby anulować wciśnij "N". \n')
        if obj == 'n':
            return False
        elif obj == 't':
            self.model.update({"date": datetime.datetime.now()})
        else:
            print('Incorrect value')
        return True
