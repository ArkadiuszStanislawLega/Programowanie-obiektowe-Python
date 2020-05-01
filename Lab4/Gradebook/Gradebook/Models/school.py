from Models.gradeLog import GradeLog
from Models.student import Student
from Models.grade import Grade
from Models.action_type import ActionType
import os


class School:
    CONSOLE_WIDTH = 80
    CONSOLE_CENTER = 40

    def __clear(self):
        return os.system('cls')

    def __highlighting_the_stage(self):
        """
        Drukuje do konsoli linie złożoną z określonego znaku.
        """
        print(self.CONSOLE_WIDTH*"*")

    def __add_new_student(self):
        """
        Wywołuje interfejs umożliwiający dodanie użytkownika.
        """
        self.__clear()
        print("Ddodaj nowego ucznia do dziennika.")
        new_student_name = input("Imię ucznia:")
        new_student_surname = input("Nazwisko ucznia:")

        new_student = Student()
        new_student.id = self.__log.get_last_id() + 1
        new_student.name = new_student_name
        new_student.surname = new_student_surname

        self.__log.add_student(new_student)
        self.__highlighting_the_stage()

    def __print_students(self):
        """
        Drukuje do konsoli wszystkich uczniów w dzienniku.
        """
        self.__clear()
        print("Dziennik - lista uczniów:")
        if len(self.__log.students) > 0:
            for student in self.__log.students:
                print(f'{student.id}. {student}')
        else:
            print("Brak uczniów w dzienniku.")
        self.__highlighting_the_stage()

    def __remove_student(self):
        pass

    def __exit(self):
        """
        Powoduje zakończenie się aplikacji.
        """
        self.__is_exit = True

    def __init__(self):
        self.__log = GradeLog()
        self.__is_exit = False

        self.__action_list = {ActionType.exit: "Wyjście",
                              ActionType.add_student: "Dodaj ucznia",
                              ActionType.remove_student: "Usuń ucznia",
                              ActionType.print_students_list:  "Lista uczni"}

        self.__actions = {ActionType.exit: self.__exit,
                          ActionType.add_student: self.__add_new_student,
                          ActionType.remove_student: self.__remove_student,
                          ActionType.print_students_list:  self.__print_students}

        self.__clear()

        while not self.__is_exit:
            try:
                print(self.CONSOLE_CENTER*' ' + 'MENU')
                self.__highlighting_the_stage()
                for i, action in enumerate(self.__action_list):
                    print(f'{i}. {self.__action_list[action]}')

                self.__highlighting_the_stage()
                user_input = int(input("Wykonaj czynność o numerze: "))

                self.__actions.get(ActionType(user_input))()

            except (ValueError):
                self.__clear()
                print(
                    "Podana wartość musi być cyfrą całkowitą dodatnią i musi być liczbą o wartości wydrukowanej w MENU.")
