from Views.view import View
from Views.label import Label
import os


class GradeView(View):

    def __init__(self, model):
        super().__init__(name="GradeView", model=model)

        self.add_component(Label("id", model.id, title="Id:"))
        self.add_component(Label("name", model.name, title="Nazwa oceny:"))
        self.add_component(Label("grade", model.grade, title="Ocena:"))
        self.add_component(
            Label("date", model.date, title="Data wystawienia:"))

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            self._component_list.get(key).update(value)
        self.show()

    def show(self):
        os.system('cls')
        for comp in self._component_list.values():
            comp.show()
