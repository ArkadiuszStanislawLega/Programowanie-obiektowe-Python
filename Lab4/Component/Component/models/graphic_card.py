from models.element import Element


class GraphicCard(Element):
    def __init__(self):
        super().__init__()
        self._id = "H699F4G4M"
        self._producent_name = "AMD Radeon"
        self._name = "HD 6900 Series"
        self._price = 199
