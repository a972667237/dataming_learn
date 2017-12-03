from PIL import Image

class ImageDealer:
    def __init__(self, img):
        self.img = img
    def toTwo(self):
        pixels = self.img.load()
        res = []
        for x in range(self.img.width):
            col = []
            for y in range(self.img.height):
                pixels[x, y] = 0 if pixels[x, y] > 125 else 1
                col.append(pixels[x, y])
            res.append(col)
        return res
