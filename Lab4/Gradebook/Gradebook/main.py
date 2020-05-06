from Models.school_class import SchoolClass
from Views.school_class_view import SchoolClassView
from Controllers.school_class_controller import SchoolClassController


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
