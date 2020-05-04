from Views.view import View
from Views.label import Label


class GradeView(View):
    VALUE_ID = "id"
    VALUE_NAME = "name"
    VALUE_GRADE = "grade"
    VALUE_DATE = "date"

    def __init__(self, model):
        super().__init__(name="GradeView", model=model)

        self.add_component(Label(self.VALUE_ID, model.id))
        self.add_component(Label(self.VALUE_NAME, model.name))
        self.add_component(Label(self.VALUE_GRADE, model.grade))
        self.add_component(Label(self.VALUE_DATE, model.date))

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for value in kwargs.get("kwargs").values():

            if value.get(self.VALUE_ID):
                self._component_list.get(self.VALUE_ID).update(
                    value.get(self.VALUE_ID))

            elif value.get(self.VALUE_NAME):
                self._component_list.get(self.VALUE_NAME).update(
                    value.get(self.VALUE_NAME))

            elif value.get(self.VALUE_GRADE):
                self._component_list.get(self.VALUE_GRADE).update(
                    value.get(self.VALUE_GRADE))

            elif value.get(self.VALUE_DATE):
                self._component_list.get(self.VALUE_DATE).update(
                    value.get(self.VALUE_DATE))

        self.show()

    def show(self):
        for comp in self._component_list.values():
            comp.show()
