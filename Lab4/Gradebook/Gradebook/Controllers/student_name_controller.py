from Controllers.controller import Controller


class StudentNameController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        print(f'Edycja nazwiska ucznia: {self._model}')
        print(80*"=")
        user_input = input(
            'Podaj nowe imię ucznia: ')
        print(80*"=")
        self._model.modify(name=user_input)
