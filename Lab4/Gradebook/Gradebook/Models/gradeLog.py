from .student import Student
from .grade import Grade


class GradeLog:

    def __init__(self):
        self.__students = []

    def add_student(self, student: Student):
        """
        Dodaje studenta do dziennika.
        Arguments:
            student {Student} -- Nowy student który ma zostać dodany do dziennika.
        """
        if isinstance(student, Student):
            if student.id not in self.__students:
                print(f'Dodaję nowego ucznia: {student.full_name}')
                self.__students.append(student)
            else:
                print(
                    f'Istnieje już student z numerem identyfikacyjnym {student.id} w dzienniku.')

    def get_last_id(self):
        """
        Zwraca najwyższy numer id z dziennika jeżeli są już jacyś uczniowie przypisani do dziennika.
        Jeżeli nie ma uczni w dzienniku to jest zwracane 0.

        Returns:
            [int] -- Najwyższy numer id w dzienniku. 
        """
        if len(self.__students) > 0:
            greatest_value = 0
            for student in self.__students:
                if student.id > greatest_value:
                    greatest_value = student.id

            return greatest_value
        else:
            return 0

    @property
    def students(self):
        return self.__students
