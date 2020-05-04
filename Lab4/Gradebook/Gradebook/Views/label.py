from Views.view import View


class Label(View):
    def __init__(self, name, model):
        super().__init__(name=name, model=model)

    def add_component(self, comp):
        if comp.name not in self._component_list:
            self._component_list[comp.name] = comp

    def update(self, *args, **kwargs):
        for value, key in kwargs:
            self._model.modify({value: key})

    def show(self):
        print(self._model)
