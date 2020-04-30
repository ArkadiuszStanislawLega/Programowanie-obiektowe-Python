from models.pc import Pc
from models.graphic_card import GraphicCard
from models.keyboard import Keyboard
from models.monitor import Monitor


def main():
    pc = Pc()

    pc.add_element(GraphicCard())
    pc.add_element(Keyboard())
    pc.add_element(Monitor())

    print(pc)


if '__main__' == __name__:
    main()
