from Controllers.controller import Controller
from Controllers.student_add_grade_controller import StudentAddGradeController
from Controllers.student_name_controller import StudentNameController
from Controllers.student_surname_controller import StudentSurnameController
from Controllers.student_edit_grades_controller import StudentEditGradesController


class StudentController(Controller):
    def __init__(self, view, model):
        super().__init__(view=view, model=model)

        self.__student_name_controller = StudentNameController(
            model=model, view=view)
        self.__student_surname_controller = StudentSurnameController(
            model=model, view=view)
        self.__student_add_grade_controller = StudentAddGradeController(
            model=model, view=view)
        self.__studen_edit_grades_controll = StudentEditGradesController(
            model=model, view=view)

        self.__is_exit = False

        options = ["Anuluj", "Zmień imię", "Zmień nazwisko",
                   "Dodaj stopnie", "Edytuj Stopnie", "Wyświetl Profil"]
        while not self.__is_exit:
            for i, value in enumerate(options):
                print(f'{i}. {value}')

            user_input = int(input("Wybierz opcję: "))
            if user_input > 0:
                if user_input == 1:
                    self.update_name()

                elif user_input == 2:
                    self.update_surname()

                elif user_input == 3:
                    self.add_grade()

                elif user_input == 4:
                    self.update_grades()

                elif user_input == 5:
                    self.view.show(refresh_mode=True)

            elif user_input == 0:
                self.__is_exit = True

    def update_name(self):
        self.__student_name_controller.get_user_input()

    def update_surname(self):
        self.__student_surname_controller.get_user_input()

    def add_grade(self):
        self.__student_add_grade_controller.get_user_input()

    def update_grades(self):
        self.__studen_edit_grades_controll.get_user_input()

    def get_user_input(self):
        pass
