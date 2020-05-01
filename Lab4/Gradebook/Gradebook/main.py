from Models.gradeLog import GradeLog
from Models.student import Student
from Models.grade import Grade
import os


def clear(): return os.system('cls')


action_list = ["Wyjście", "Dodaj ucznia"]

log = GradeLog()


def add_new_user():
    clear()
    print("Ddodaj nowego ucznia do dziennika.")
    new_student_name = input("Imię ucznia:")
    new_student_surname = input("Nazwisko ucznia:")

    new_student = Student()
    new_student.name = new_student_name
    new_student.surname = new_student_surname

    log.add_student(new_student)


def main():

    # Flaga wskazująca czy program ma się zakończyć
    is_exit = False

    while not is_exit:
        try:
            for i, action in enumerate(action_list):
                print(f'{i}. {action}')
            user_input = int(input("Wykonaj czynność o numerze: "))

            if user_input == 0:
                is_exit = True

            elif user_input == 1:
                add_new_user()

            else:
                "Podanej wartości nie ma na liście wyborów."
        except (ValueError):
            print("Podana wartość musi być cyfrą całkowitą dodatnią.")

    # student = Student()
    # student.id = 1
    # student.name = "Mietek"
    # student.surname = "Nowak"
    # student.add_grade(Grade.ndst)
    # student.add_grade(Grade.dst)
    # student.add_grade(Grade.bdb)
    # student.add_grade(Grade.dop)
    # student.add_grade(Grade.ndst)

    # student2 = Student()
    # student2.id = 2
    # student2.name = "Marcin"
    # student2.surname = "Szcześniak"
    # student2.add_grade(Grade.bdb)
    # student2.add_grade(Grade.ndst)
    # student2.add_grade(Grade.dst)
    # student2.add_grade(Grade.dop)
    # student2.add_grade(Grade.db)

    # student3 = Student()
    # student3.id = 3
    # student3.name = "Kamil"
    # student3.surname = "Kowalski"
    # student3.add_grade(Grade.ndst)
    # student3.add_grade(Grade.ndst)
    # student3.add_grade(Grade.dop)
    # student3.add_grade(Grade.dop)
    # student3.add_grade(Grade.ndst)
    # student3.add_grade(Grade.bdb)

    # student4 = Student()
    # student4.id = 3

    # log.add_student(student)
    # log.add_student(student2)
    # log.add_student(student3)
    # log.add_student(student4)

    # print(80*"*")
    # for log_student in log.students.values():
    #     log_student.print_grades()
    #     print(
    #         f'Średnia ocen {log_student.full_name} {log_student.average_grade}')
    #     print(80*"-")

    # print(log.students)


if __name__ == "__main__":
    main()
