from Views.view import View
from Views.label import Label
import os


class StudentView(View):

    def __init__(self, model):
        super().__init__(name="StudentView", model=model)

        self.add_component(Label("id", model.id, title="Id:"))
        self.add_component(Label("name", model.name, title="Imię:"))
        self.add_component(Label("surname", model.surname, title="Nazwisko:"))
        self.add_component(
            Label("average", model.average_grade, title="Średnia ocen:"))
        self.add_component(Label("add_grade", model.grades,
                                 title="Ostatnio dodana ocena:"))

        self.__all_grades = ""

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def refresh_average(self):
        self._component_list.get("average").update(
            round(self._model.average_grade, 2))

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            self._component_list.get(key).update(value)
            if key == "add_grade":
                self.refresh_average()
        self.show()

    def show(self, refresh_mode=False):
        os.system('cls')
        if refresh_mode:
            self.refresh_average()

        for comp in self._component_list.values():
            comp.show()

        print("Wszystkie oceny:")
        print(*self._model.grades.values(), sep="\n")
        print(80*"=")
