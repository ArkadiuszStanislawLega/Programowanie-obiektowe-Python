from models.pc import Pc
from models.graphic_card import GraphicCard
from models.keyboard import Keyboard
from models.monitor import Monitor
from models.motherboard import Motherboard
from models.mouse import Mouse


def main():
    pc = Pc()

    pc.add_element(Motherboard())
    pc.add_element(GraphicCard())
    pc.add_element(Keyboard())
    pc.add_element(Monitor())
    pc.add_element(Mouse())

    print(pc)


if '__main__' == __name__:
    main()
