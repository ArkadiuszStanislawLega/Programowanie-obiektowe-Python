from Models.school import School
from Models.grade import Grade
from Models.student import Student
from Models.school_class import SchoolClass
from Views.grade_view import GradeView
from Views.student_view import StudentView
from Views.school_class_view import SchoolClassView
from Controllers.grade_controller import GradeController
from Controllers.student_controller import StudentController
from Controllers.school_class_controller import SchoolClassController
from Enums.grade_type import GradeType


def main():
    school_class = SchoolClass()
    school_class.id = 1
    school_class.name = "1B"

    view = SchoolClassView(school_class)
    school_class.add_observer(view)
    view.show()

    SchoolClassController(view=view, model=school_class)


if __name__ == "__main__":
    main()
