from Models.student import Student
from Models.grade_type import GradeType


class GradeLog:

    def __init__(self):
        self.__students = {}

    def add_student(self, student: Student):
        """
        Dodaje studenta do dziennika.
        Arguments:
            student {Student} -- Nowy student który ma zostać dodany do dziennika.
        """
        if isinstance(student, Student):
            if student.id not in self.__students:
                print(f'Dodaję nowego ucznia: {student.full_name}')
                self.__students[student.id] = student
            else:
                print(
                    f'Istnieje już student z numerem identyfikacyjnym {student.id} w dzienniku.')

    def remove_student(self, id: int):
        """
        Usuwa ucznia z dziennika o podanym w argumencie numerze id.

        Arguments:
            id {int} -- Numer ucznia id do usunięcia.
        """
        if isinstance(id, int) and id > 0:
            print(f'Usuwam ucznia z dziennika: {self.__students.get(id)}')
            self.__students.pop(id)

    def print_students_list(self):
        for student in self.__students.values():
            print(f'{student.id}. {student}')

    def get_last_id(self):
        """
        Zwraca najwyższy numer id z dziennika jeżeli są już jacyś uczniowie przypisani do dziennika.
        Jeżeli nie ma uczni w dzienniku to jest zwracane 0.

        Returns:
            [int] -- Najwyższy numer id w dzienniku. 
        """
        if len(self.__students) > 0:
            greatest_value = 0
            for id in self.__students.keys():
                if id > greatest_value:
                    greatest_value = id

            return greatest_value
        else:
            return 0

    def exibit_a_grade_to_the_student(self, student_id: int, grade: GradeType):
        if isinstance(student_id, int) and isinstance(grade, GradeType):
            self.__students.get(student_id).add_grade(grade)

    @property
    def students(self):
        return self.__students
