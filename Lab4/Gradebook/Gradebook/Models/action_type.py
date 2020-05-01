from enum import Enum


class ActionType(Enum):
    """
    Akcje które są wykonywane w czasie działania aplikacji
    """
    # Wyjście z programu
    exit = 0
    # Dodawanie nowego ucznia do dziennika
    add_student = 1
    # Usuwanie ucznia z dziennika
    remove_student = 2
    # Drukowanie wszystkich uczniów w konsoli
    print_students_list = 3
    # Edytowanie ucznia
    edit_student = 4
    # Wstawianie ocen
    issuing_grades = 5
    # Wyświetlanie średnich ocen
    average_grades = 6
