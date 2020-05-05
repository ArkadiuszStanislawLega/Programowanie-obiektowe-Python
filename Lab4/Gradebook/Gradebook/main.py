from Models.school import School
from Models.grade import Grade
from Models.student import Student
from Views.grade_view import GradeView
from Views.student_view import StudentView
from Controllers.grade_controller import GradeController
from Controllers.student_controller import StudentController
from Enums.grade_type import GradeType


def main():
    # School()
    grade = Grade()

    grade.id = "1"
    grade.name = "Sprawdzian"
    grade.grade = GradeType.bdb

    student = Student()
    student.id = 1
    student.name = "Mietek"
    student.surname = "Szcześniak"

    view = StudentView(student)
    student_controller = StudentController(view=view, model=student)

    student.add_observer(view)

    view.show()

    student_controller.update_name()
    print(80*"=")

    student_controller.update_surname()
    print(80*"=")

    student_controller.add_grade()
    print(80*"=")


if __name__ == "__main__":
    main()
