from Controllers.controller import Controller
from Enums.grade_type import GradeType
from Enums.grade_properties_type import GradePropertiesType


class GradeGradeController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

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

        try:

            user_select = int(input("Ocena którą chcesz wstawić: "))
            print(80*"=")
            if user_select > 0:
                self._model.modify(grade=GradeType(user_select))

        except(ValueError):
            print("Błędna wartość.")
