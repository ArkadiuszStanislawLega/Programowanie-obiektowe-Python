from Models.modification import Modification
from cv2 import blur


class Blur(Modification):
    def action(self, img):
        if img is not None:
            print("Dodaje rozmycie.")
            return blur(img, (20, 40))
