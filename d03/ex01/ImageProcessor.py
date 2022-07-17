import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# https://matplotlib.org/stable/tutorials/introductory/images.html


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        try:
            img = mpimg.imread(path)
            print("Loading image of dimensons", len(img[0]), "x", len(img[1]))
            return numpy.array(img)
        except Exception as e:
            print("Error:", e)
            return None

    def display(self, array):
        try:
            plt.imshow(array)
            plt.show()
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("42AI.png")
    # Loading image of dimensions 200 x 200
    print(arr)
    imp.display(arr)