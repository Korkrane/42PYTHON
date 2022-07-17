import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from FileLoader import FileLoader

class MyPlotLib:
    def __init__(self):
        pass

    def histogram(self, data, features):
        try:
            if len(features) == 1:
                y = data[features[0]].tolist()
                plt.hist(y, 15, density=False, facecolor='b', alpha=0.75)
                plt.title(features[0])
                plt.grid(True)
            else:
                axis = plt.subplots(1, len(features), figsize=(10, 5))[1]
                for i, elem in enumerate(features):
                    y = data[elem].tolist()
                    axis[i].hist(y, 15, density=False, facecolor='b', alpha=0.75)
                    axis[i].set_title(elem)
                    axis[i].grid(True)
            plt.show()
        except Exception as e:
            print(e)

    def density(self, data, features):
        try:
            axis = plt.subplots(figsize=(10, 5))[1]
            for elem in features:
                pd.DataFrame(data[elem]).plot(ax=axis, kind='density')
            plt.show()
        except Exception as e:
            print(e)

    def pair_plot(self, data, features):
        try:
            sns.pairplot(data.filter(items=features), diag_kind = 'hist', diag_kws = {'bins':10})
            plt.show()
        except Exception as e:
            print(e)

    def box_plot(self, data, features):
        try:
            data.boxplot(column=features, grid=False, figsize=(10, 5))
            plt.show()
        except Exception as e:
            print(e)

loader = FileLoader()
data = loader.load("../athlete_events.csv")
mpl = MyPlotLib()
mpl.histogram(data, ['Height', 'Weight'])
# mpl.density(data, ['Weight', 'Height'])
mpl.pair_plot(data, ['Weight', 'Height'])
# mpl.box_plot(data, ['Weight', 'Height'])
