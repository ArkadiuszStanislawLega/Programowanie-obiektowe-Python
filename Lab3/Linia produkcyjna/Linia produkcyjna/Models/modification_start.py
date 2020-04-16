from Models.modification import Modification
from Models.rotate90 import Rotate90
from Models.rotate180 import Rotate180
from Models.blur import Blur
from Models.modification_end import ModificationEnd
from cv2 import imread, imwrite, rotate, ROTATE_180


class ModificationStart(Modification):
    PICTURE_PATH = 'test.jpg'

    def __init__(self):

        rot90 = Rotate90()
        rot180 = Rotate180()
        blur = Blur()
        modification_end = ModificationEnd()

        modification_end.action(blur.action(rot180.action(
            rot90.action(self.action(self.PICTURE_PATH)))))

    def action(self, img):
        print("Rozpoczynam obróbkę.")
        return imread(img)
