from Controllers.controller import Controller
from Models.grade import Grade
from Views.grade_view import GradeView
from Enums.grade_type import GradeType
import datetime


class StudentAddGradeController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

    def get_user_input(self):
        print(f'Dodawanie stopnia uczniowi: {self._model} ')
        print(80*"=")
        user_name_of_grade = input("Podaj nazwę oceny: ")
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

            user_grade_select = int(input("Ocena którą chcesz wstawić: "))
            print(80*"=")
            if user_grade_select > 0:
                new_grade = Grade()
                new_grade.id = f'{self._model.id}/{len(self._model.grades)+1}'
                new_grade.name = user_name_of_grade
                new_grade.grade = GradeType(user_grade_select)
                new_grade.add_observer(GradeView(new_grade))
                self._model.modify(add_grade=new_grade)
            elif user_grade_select == 0:
                print(80*"=")

        except(ValueError):
            print("Błędna wartość.")
