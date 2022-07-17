import sys
import numpy as np
import random as rd


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        if isinstance(max_iter, int) is False or \
                isinstance(ncentroid, int) is False:
            raise ValueError('invalid arguments')
        if max_iter < 0 or ncentroid < 0:
            raise ValueError('invalid arguments')
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, X):
        if isinstance(X, np.ndarray) is False:
            return None
        # enough datapoint for number of desired centroids
        if X.shape[0] < self.ncentroid:
            return None
        self.centroids = np.empty((self.ncentroid, 3))

        # define random centroids
        for i in range(self.ncentroid):
            index = rd.randint(0, X.shape[0] - 1)
            self.centroids[i] = X[index]

        # run max_iter times the kmeans algo
        # https://medium.com/nerd-for-tech/k-means-python-implementation-from-scratch-8400f30b8e5cd
        for iteration in range(self.max_iter):
            cluster = [[] for _ in range(self.ncentroid)]
            for i, point in enumerate(X):
                dist = np.empty(self.ncentroid)
                for j, centroid in enumerate(self.centroids):
                    dist[j] = np.linalg.norm(point - centroid) # dist from centroids
                cluster[np.argmin(dist)].append(point) # save it to the closest centroids
            tmp = self.centroids.copy()
            #recalculate new centroids mean to adapt them to your clusters
            for i in range(self.ncentroid):
                cluster[i] = np.array(cluster[i])
                if len(cluster[i]) != 0:
                    n = len(cluster[i])
                    self.centroids[i] = np.sum(cluster[i], axis=0) / n
            # if centroids do not change, stop the algo
            if (tmp == self.centroids).all():
                return None
        return None

    def predict(self, X):
        if isinstance(X, np.ndarray) is False or len(self.centroids) != self.ncentroid:
            return None
        predict = []
        # https://medium.com/nerd-for-tech/k-means-python-implementation-from-scratch-8400f30b8e5cd
        for point in X:
            dist = np.empty(self.ncentroid)
            for j, centroid in enumerate(self.centroids):
                dist[j] = np.linalg.norm(point - centroid)
            predict.append(self.centroids[np.argmin(dist)])
        return np.array(predict)


def parse(argv):
    names = ['filepath', 'max_iter', 'ncentroid']
    if len(argv) != 4:
        return None
    new_args = {}
    for i in range(1, len(argv)):
        tmp = argv[i].split('=')
        if len(tmp) != 2 or tmp[0] not in names:
            return None
        new_args[tmp[0]] = tmp[1]
    for name in names:
        if name not in new_args.keys():
            return None
    try:
        new_args['max_iter'] = int(new_args['max_iter'])
        new_args['ncentroid'] = int(new_args['ncentroid'])
    except Exception:
        return None
    if new_args['max_iter'] < 0 or new_args['ncentroid'] < 0:
        return None
    return new_args

def getPlanets(k):
    # set the belt
    i = np.argmax(k.centroids[:, 0])
    belt = k.centroids[i]
    # rmv belt and rmv martian cluster to let earth selection between 2 last clusters
    tmp = k.centroids.copy()
    tmp = np.delete(tmp, i, 0)
    earth = tmp.copy()
    earth = np.delete(earth, np.argmax(tmp[:, 0]), 0)
    #cuz earth are smaller than martian take the smallest between 2 cluster left
    i = np.argmin(tmp[:, 1])
    if (tmp[i] == earth[0]).all():
        earth = earth[1]
    else:
        earth = earth[0]
    #let in tmp only venus and mars clusters
    for i in range(len(tmp)):
        if (tmp[i] == earth).all():
            tmp = np.delete(tmp, i, 0)
            break
    # check which one is mars and venus clusters
    if (tmp[:, 1] < earth[1]).all() is False:
        i = np.argmin(tmp[:, 1])
        venus = tmp[i]
        mars = tmp[1 - i]
    else:
        i = np.argmax(tmp[:, 0])
        mars = tmp[i]
        venus = tmp[1 - i]
    planet = [[] for _ in range(k.ncentroid)]
    ibelt = np.where(np.all(k.centroids == belt, axis=1))[0][0]
    iearth = np.where(np.all(k.centroids == earth, axis=1))[0][0]
    imars = np.where(np.all(k.centroids == mars, axis=1))[0][0]
    ivenus = np.where(np.all(k.centroids == venus, axis=1))[0][0]
    planet[iearth] = "Asteroids' Belt colonies"
    planet[ibelt] = "United Nations of Earth"
    planet[imars] = "Mars Republic"
    planet[ivenus] = "The flying cities of Venus"
    return planet


def printData(k, predict):
    if isinstance(predict, np.ndarray) is False:
        return None
    if k.ncentroid == 4:
        planet = getPlanets(k)
        for i in range(k.ncentroid):
            count = 0
            for j in range(len(predict)):
                if (predict[j] == k.centroids[i]).all():
                    count += 1
            print('{} - {} - {} habitants'.format(k.centroids[i], planet[i], count))
    else:
        for i in range(k.ncentroid):
            count = 0
            for j in range(len(predict)):
                if (predict[j] == k.centroids[i]).all():
                    count += 1
            print('{} - {}'.format(k.centroids[i], count))

from csvreader import CsvReader

if __name__ == "__main__":
    args = parse(sys.argv)
    if args is not None:
        with CsvReader(args['filepath'], ",", True) as csv_file:
            dataset = np.array(csv_file.getdata(), dtype=float)
            dataset = np.delete(dataset, 0, 1)
            if dataset is not None:
                k = KmeansClustering(args['max_iter'], args['ncentroid'])
                k.fit(dataset)
                predict = k.predict(dataset)
                if predict is None:
                    pass
                else:
                    printData(k, predict)
    else:
        pass