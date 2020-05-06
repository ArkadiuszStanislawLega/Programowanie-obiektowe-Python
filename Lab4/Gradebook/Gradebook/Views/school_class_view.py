from Views.view import View
from Views.label import Label
import os


class SchoolClassView(View):

    def __init__(self, model):
        super().__init__(name="SchoolClassView", model=model)

        self.add_component(Label("id", model.id, title="Id:"))
        self.add_component(Label("name", model.name, title="Nazwa klasy:"))
        self.add_component(
            Label("average_grades", model.average_grade, title="Średnia ocen:"))
        self.add_component(
            Label("add_student", model.students, title="Uczniowie:"))

        self.__all_students = ""

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def refresh_average(self):
        self._component_list.get("average_grades").update(
            round(self._model.average_grade, 2))

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            self._component_list.get(key).update(value)

            os.system('cls')
            if key == "add_student":
                print(f'Aktualizacja: dodano ucznia.')
            elif key == "name":
                print(
                    f'Aktualizacja: zmiana imienia ucznia.')
            elif key == "surname":
                print(
                    f'Aktualizacja: zmiana nazwiska ucznia.')

        print(80*"=")

    def show(self, refresh_mode=False):
        os.system('cls')
        if refresh_mode:
            self.refresh_average()

        for comp in self._component_list.values():
            comp.show()

        print("Wszyscy uczniowe:")
        print(*self._model.students.values(), sep="\n")
        print(80*"=")
