from Models.modification import Modification
from cv2 import rotate, ROTATE_90_CLOCKWISE


class Rotate90(Modification):
    def action(self, img):
        if img is not None:
            print("Obracam obraz o 90 stopni.")
            return rotate(img, ROTATE_90_CLOCKWISE)
