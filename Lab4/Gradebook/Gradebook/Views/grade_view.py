from Views.view import View
from Views.label import Label


class GradeView(View):
    def __init__(self, model):
        super().__init__(name="GradeView", model=model)
        self.add_component(Label("id", model.id))
        self.add_component(Label("name", model.name))
        self.add_component(Label("grade", model.grade))
        self.add_component(Label("date", model.date))

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for value, key in kwargs:
            self._component_list.get(key).update({key: value})

    def show(self):
        for comp in self._component_list.values():
            comp.show()
