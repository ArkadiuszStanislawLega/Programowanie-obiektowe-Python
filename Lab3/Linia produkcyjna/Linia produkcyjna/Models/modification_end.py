from Models.modification import Modification
import sys
from cv2 import imread, imwrite, rotate, ROTATE_90_CLOCKWISE
import numpy as np


class ModificationEnd(Modification):
    def action(self, img):
        if img is not None:
            print("Kończę modyfikacje i zapisuję obraz.")
            return imwrite('img.jpg', img)
