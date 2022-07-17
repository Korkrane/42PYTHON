from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

imp = ImageProcessor()

cf = ColorFilter()

for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
	array = plt.imread("./elon_canaGAN.png")
	plt.imshow(f(array))
	plt.show()

im = cf.to_grayscale(array, "m")
plt.imshow(im, cmap="gray")
plt.show()

im = cf.to_grayscale(array, "w", weights=[0.2126, 0.7152, 0.0722])
plt.imshow(im, cmap="gray")
plt.show()