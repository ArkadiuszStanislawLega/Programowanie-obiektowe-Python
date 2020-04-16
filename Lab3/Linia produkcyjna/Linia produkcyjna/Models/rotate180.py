from Models.modification import Modification
from cv2 import rotate, ROTATE_180


class Rotate180(Modification):
    def action(self, img):
        if img is not None:
            print("Obracam obraz o 180 stopni.")
            return rotate(img, ROTATE_180)
