from Models.school import School
from Models.grade import Grade
from Views.grade_view import GradeView
from Controllers.grade_date_controller import GradeDateController
from Controllers.grade_grade_controller import GradeGradeController
from Controllers.grade_id_controller import GradeIdController
from Controllers.grade_name_controller import GradeNameController
from Enums.grade_type import GradeType


def main():
    # School()
    grade = Grade()

    grade.id = "1"
    grade.name = "Sprawdzian"
    grade.grade = GradeType.bdb

    view = GradeView(grade)

    grade_id_controller = GradeIdController(model=grade, view=view)
    grade_name_controller = GradeNameController(model=grade, view=view)
    grade_grade_controller = GradeGradeController(model=grade, view=view)
    grade_date_controller = GradeDateController(model=grade, view=view)

    for child in view.get_children():
        grade.add_observer(child)

    view.show()

    grade_name_controller.get_user_input()
    grade_grade_controller.get_user_input()
    grade_date_controller.get_user_input()

    view.show()


if __name__ == "__main__":
    main()
