from Models.gradeLog import GradeLog
from Models.student import Student
from Models.grade_type import GradeType
from Models.action_type import ActionType
import os


class School:
    # Maksymalna wartość drukowanych ozdobników w konsoli.
    CONSOLE_WIDTH = 80
    # Umownny środek konsoli do drukowania informacji.
    CONSOLE_CENTER = 40

    def __init__(self):
        self.__log = GradeLog()
        self.__is_exit = False

        self.__action_list = {ActionType.exit: "Wyjście",
                              ActionType.add_student: "Dodaj ucznia",
                              ActionType.remove_student: "Usuń ucznia",
                              ActionType.print_students_list:  "Lista uczni",
                              ActionType.edit_student: "Edytuj ucznia"}

        self.__actions = {ActionType.exit: self.__exit,
                          ActionType.add_student: self.__add_new_student,
                          ActionType.remove_student: self.__remove_student,
                          ActionType.print_students_list:  self.__print_students,
                          ActionType.edit_student: self.__edit_student}

        self.__clear()
        self.__run()

    def __print_warning(self):
        """
        Drukuje informacje związaną z podanym błędnym numerm zadania dla aplikacji.
        """
        print("Podano błędną wartość. Podaj wartość numeru z MENU.")

    def __clear(self):
        """
        Czyści konsole.
        """
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
        new_student_name = input("Imię ucznia: ")
        new_student_surname = input("Nazwisko ucznia: ")

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
            self.__log.print_students_list()
        else:
            print("Brak uczniów w dzienniku.")

        self.__highlighting_the_stage()

    def __remove_student(self):
        """
        Wywołuje interfejs umożliwiający usunięcie użytkownika.
        """
        try:
            print("Dziennik - usuń ucznia:")
            self.__print_students()
            user_input = int(input("Podaj numer identyfikacyjny ucznia: "))
            self.__log.remove_student(user_input)
        except (ValueError):
            self.__clear()
            self.__print_warning()

    def __edit_student(self):
        """
        Wyowułuje interfejs użytkownika umożliwający zmianę danych uczniów.
        """
        try:
            # Flaga wskazująca czy pętla edycji użytkownika się zakończyła.
            is_exit = False
            # Wartości które wyświetlają się w menu - informacje o tym co można edytować.
            values = ["Wyjdź do menu", "Imię", "Nazwisko"]

            print("Dziennik - edytuj ucznia:")
            self.__highlighting_the_stage()
            self.__print_students()

            user_input = int(input("Podaj numer identyfikacyjny ucznia: "))
            student = self.__log.students.get(user_input)

            self.__clear()

            while not is_exit:
                self.__highlighting_the_stage()
                print("Dziennik - edytuj ucznia:")
                print(f'Edytujesz dane ucznia: {student}')
                self.__highlighting_the_stage()

                for i, value in enumerate(values):
                    print(f'{i}. {value}')

                edit_value = int(
                    input("Podaj numer z listy, wartości którą chcesz edytować: "))
                if edit_value == 0:
                    is_exit = True
                elif edit_value == 1:
                    student.name = input("Podaj nowe imię: ")
                elif edit_value == 2:
                    student.surname = input("Podaj nowe nazwisko: ")

                self.__clear()
                print("Wartości zostały zmienione.")

        except (ValueError):
            self.__clear()
            self.__print_warning()

    def __exit(self):
        """
        Powoduje zakończenie się aplikacji.
        """
        self.__is_exit = True

    def __run(self):
        """
        Uruchamia pętlę aplikacji.
        """
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
                self.__print_warning()
