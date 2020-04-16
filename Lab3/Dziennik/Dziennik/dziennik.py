from Models.gradeLog import GradeLog
from Models.student import Student
from Models.grade import Grade


def main():
    log = GradeLog()

    student = Student()
    student.id = 1
    student.name = "Mietek"
    student.surname = "Nowak"
    student.add_grade(Grade.ndst)
    student.add_grade(Grade.dst)
    student.add_grade(Grade.bdb)
    student.add_grade(Grade.dop)
    student.add_grade(Grade.ndst)

    student2 = Student()
    student2.id = 2
    student2.name = "Marcin"
    student2.surname = "Szcześniak"
    student2.add_grade(Grade.bdb)
    student2.add_grade(Grade.ndst)
    student2.add_grade(Grade.dst)
    student2.add_grade(Grade.dop)
    student2.add_grade(Grade.db)

    student3 = Student()
    student3.id = 3
    student3.name = "Kamil"
    student3.surname = "Kowalski"
    student3.add_grade(Grade.ndst)
    student3.add_grade(Grade.ndst)
    student3.add_grade(Grade.dop)
    student3.add_grade(Grade.dop)
    student3.add_grade(Grade.ndst)
    student3.add_grade(Grade.bdb)

    student4 = Student()
    student4.id = 3

    log.add_student(student)
    log.add_student(student2)
    log.add_student(student3)
    log.add_student(student4)

    print(80*"*")
    for log_student in log.students.values():
        log_student.print_grades()
        print(
            f'Średnia ocen {log_student.full_name} {log_student.average_grade}')
        print(80*"-")

    print(log.students)


if __name__ == "__main__":
    main()
