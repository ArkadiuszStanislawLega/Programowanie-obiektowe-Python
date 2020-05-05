from Views.view import View
from Views.label import Label


class StudentView(View):

    def __init__(self, model):
        super().__init__(name="StudentView", model=model)

        self.add_component(Label("id", model.id))
        self.add_component(Label("name", model.name))
        self.add_component(Label("surname", model.surname))

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            self._component_list.get(key).update(value)

        self.show()

    def show(self):
        for comp in self._component_list.values():
            comp.show()
