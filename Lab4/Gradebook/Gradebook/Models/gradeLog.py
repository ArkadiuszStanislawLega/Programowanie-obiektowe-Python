from .student import Student
from .grade import Grade


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

    @property
    def students(self):
        return self.__students
