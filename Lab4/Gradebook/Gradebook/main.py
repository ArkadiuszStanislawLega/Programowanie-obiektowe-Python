from Models.school import School
from Models.grade import Grade
from Views.grade_view import GradeView
from Controllers.grade_controller import GradeController
from Enums.grade_type import GradeType


def main():
    # School()
    grade = Grade()

    grade.id = "1"
    grade.name = "Sprawdzian"
    grade.grade = GradeType.bdb

    view = GradeView(grade)
    grade_controller = GradeController(view=view, model=grade)

    grade.add_observer(view)

    view.show()

    grade_controller.update_name()
    grade_controller.update_grade()
    grade_controller.update_date()

    view.show()


if __name__ == "__main__":
    main()
