from __future__ import print_function

import math
import random
import numpy


class Cluster(object):

    def __init__(self, center):
        self.center = center
        self.data = []  # podaci koji pripadaju ovom klasteru

    def recalculate_center(self):
        # TODO 1: implementirati racunanje centra klastera
        # centar klastera se racuna kao prosecna vrednost svih podataka u klasteru

        if not self.data:
            return

        self.center = [0] * len(self.data[0])

        for x in self.data:
            for i in range(len(x)):
                self.center[i] = self.center[i] + x[i]

        for i in range(len(self.center)):
            self.center[i] = self.center[i] / len(self.data)


class KMeans(object):

    def __init__(self, n_clusters, max_iter):
        """
        :param n_clusters: broj grupa (klastera)
        :param max_iter: maksimalan broj iteracija algoritma
        :return: None
        """
        self.data = None
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.clusters = []

    def fit(self, data):
        self.data = data  # lista N-dimenzionalnih podataka
        # TODO 4: normalizovati podatke pre primene k-means

        for x in self.data:
            x = (x - numpy.mean(x)) / numpy.std(x)

        # TODO 1: implementirati K-means algoritam za klasterizaciju podataka
        # kada algoritam zavrsi, u self.clusters treba da bude "n_clusters" klastera (tipa Cluster)

        # select centers
        for i in range(self.n_clusters):
            self.clusters.append(Cluster([random.randint(0, 5) for i in range(len(data[0]))]))

        for i in range(self.max_iter):
            for cluster in self.clusters:
                cluster.data.clear()

            for data in self.data:
                index = self.predict(data)
                self.clusters[index].data.append(data)

            for cluster in self.clusters:
                cluster.recalculate_center()

        # TODO (domaci): prosiriti K-means da stane ako se u iteraciji centri klastera nisu pomerili

    def predict(self, data):
        # TODO 1: implementirati odredjivanje kom klasteru odredjeni podatak pripada
        # podatak pripada onom klasteru cijem je centru najblizi (po euklidskoj udaljenosti)
        # kao rezultat vratiti indeks klastera kojem pripada

        min_distance = euclidean_distance(self.clusters[0].center, data)
        cluster_index = 0

        for i in range(self.n_clusters):
            new_distance = euclidean_distance(self.clusters[i].center, data)

            if new_distance < min_distance:
                min_distance = new_distance
                cluster_index = i

        return cluster_index

    def sum_squared_error(self):
        # TODO 3: implementirati izracunavanje sume kvadratne greske
        # SSE (sum of squared error)
        # unutar svakog klastera sumirati kvadrate rastojanja izmedju podataka i centra klastera

        sum = 0

        for cluster in self.clusters :
            for x in cluster.data :
                sum = sum + numpy.power(numpy.linalg.norm(x - cluster.center), 2)

        return sum / len(self.clusters)


def euclidean_distance(a, b):
    return math.sqrt(math.pow((a[0] - b[0]),2) + (math.pow((a[1] - b[1]),2)))
