from Controllers.controller import Controller


class GradeNameController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        user_input = input(
            'Podaj nową nazwę oceny: \n')
        self._model.modify({"name": user_input})
