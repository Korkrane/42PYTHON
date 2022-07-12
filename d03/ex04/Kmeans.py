import random
import numpy as np
import sys
from csvreader import CsvReader
import matplotlib.pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    def display3d(self, X):
        """
        Show the clusters.
        """
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('Height')
        ax.set_ylabel('Weight')
        ax.set_zlabel('Bone_density')
        colors = ['r', 'g', 'b', 'y']
        for i in range(self.ncentroid):
            ax.scatter(X[self.clusters[i]][:, 0],
                       X[self.clusters[i]][:, 1],
                       X[self.clusters[i]][:, 2],
                       c=colors[i])
            ax.scatter(self.centroids[i][0],
                       self.centroids[i][1],
                       self.centroids[i][2],
                       c=colors[i], marker='*')
        plt.show()

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(X, np.ndarray):
            return None
        centroid_idx = np.array((random.sample(range(len(X)),
                                k=self.ncentroid)))
        self.centroids = np.array([X[idx] for idx in centroid_idx])
        for i in range(self.max_iter):
            if i is not 0 and (old_centroids == self.centroids).all():
                break
            old_centroids = np.copy(self.centroids)
            self.predict(X)
            for k in range(self.ncentroid):
                self.centroids[k] = np.mean(X[self.clusters[k]], axis=0)
        if (self.ncentroid == 4):
            self.display3d(X)
        print("Centroid populations:")
        for k in range(self.ncentroid):
            print(k, ":", len(self.clusters[k]))
        return None

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.clusters = list([] for i in range(self.ncentroid))
        ret = np.zeros(len(X), dtype=int)
        for j in range(len(X)):
            min_dist = sys.maxsize
            min_idx = None
            for k in range(self.ncentroid):
                dist = sum(abs(X[j][idx] - self.centroids[k][idx])
                           for idx in range(len(X[j])))
                if dist < min_dist:
                    min_dist = dist
                    min_idx = k
            self.clusters[min_idx].append(j)
            ret[j] = min_idx
        return ret


if __name__ == '__main__':
    try:
        assert(len(sys.argv) == 4), "Wrong parameters number"
        assert(sys.argv[1].startswith('filepath=')), "filepath parameter error"
        assert(sys.argv[2].startswith('ncentroid=')), "ncentroid parameter error"
        assert(sys.argv[3].startswith('max_iter=')), "max_iter parameter error"

        filePath = sys.argv[1].partition('=')[2]
        ncentroid = int(sys.argv[2].partition('=')[2])
        max_iter = int(sys.argv[3].partition('=')[2])

        assert(isinstance(max_iter, int) and max_iter > 0), "max_iter parameter error"
        assert(isinstance(ncentroid, int) and ncentroid > 0), "ncentroid parameter error"
        print(filePath)
        print(max_iter)
        print(ncentroid)
        with CsvReader(filePath, ',', True) as file:
            assert file, "File error"
            kmean = KmeansClustering(max_iter, ncentroid)
            arr = np.array(file.getdata(), dtype=float)
            print(kmean.__dict__)
            kmean.fit(arr)
    except Exception as e:
        print(e)
