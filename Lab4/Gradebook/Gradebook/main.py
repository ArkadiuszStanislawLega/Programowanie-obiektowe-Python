from Models.school import School
from Models.grade import Grade
from Models.student import Student
from Views.grade_view import GradeView
from Views.student_view import StudentView
from Controllers.grade_controller import GradeController
from Controllers.student_controller import StudentController
from Enums.grade_type import GradeType


def main():
    student = Student()
    student.id = 1
    student.name = "Mietek"
    student.surname = "Szcześniak"

    view = StudentView(student)
    student.add_observer(view)

    StudentController(view=view, model=student)

    student.print_grades()


if __name__ == "__main__":
    main()
