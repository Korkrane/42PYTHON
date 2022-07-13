import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from FileLoader import FileLoader


class MyPlotLib:
    def __init__(self):
        pass

    def histogram(self, data, **features):
        try:
            data.plot.hist(bins=10)
            plt.show()
            return
        except Exception as e:
            print("Error :", e)

    def density(self, data, **features):
        try:
            return
        except Exception as e:
            print("Error :", e)

    def pair_plot(self, data, **features):
        try:
            return
        except Exception as e:
            print("Error :", e)

    def box_plot(self, data, **features):
        try:
            return
        except Exception as e:
            print("Error :", e)

loader = FileLoader()
data = loader.load("../athlete_events.csv")
mpl = MyPlotLib()
mpl.histogram(data, bins=10)
