from Controllers.controller import Controller
from Enums.grade_type import GradeType


class GradeGradeController(Controller):
    def __init__(self, view, model):
        super().__init__(view, model)

    def get_user_input(self):
        grades = ["Anuluj",
                  GradeType.ndst,
                  GradeType.dop,
                  GradeType.dst,
                  GradeType.db,
                  GradeType.bdb
                  ]

        for i, value in enumerate(grades):
            print(f'{i}. {value}')

        user_select = int(input("Ocena którą chcesz wstawić: "))

        if user_select > 0:
            self._model.update({"grade": GradeType(user_select)})
