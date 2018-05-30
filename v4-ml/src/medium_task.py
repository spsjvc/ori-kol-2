import os
import csv
import matplotlib.pyplot as plt

from kmeans import KMeans

def print_point_info(point, cluster, cluster_idx):
    print('Tacka: ({0}, {1})'.format(point[0], point[1]))
    print('Redni broj klastera: {0}'.format(cluster_idx))
    print('Koordinate centra: ({0}, {1})'.format(cluster.center[0], cluster.center[1]))
    print()


if __name__ == '__main__':
    points_for_info = [[425, 170], [477, 10.2], [3292, 11.7], [220, 58]]

    # read data
    data = []

    with open(os.path.join(os.path.dirname(__file__), '../data/data2.csv')) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data.append([float(row['income']), float(row['infant'])])

    # plot data
    plt.figure()
    for x in data:
        plt.scatter(x[0], x[1])

    plt.xlabel('income')
    plt.ylabel('infant')
    plt.show()

    # k-means
    kmeans = KMeans(n_clusters=4, max_iter=20)
    kmeans.fit(data)

    colors = {0: 'red', 1: 'green', 2: 'yellow', 3: 'blue'}
    plt.figure()
    for idx, cluster in enumerate(kmeans.clusters):
        # plot centers
        plt.scatter(cluster.center[0], cluster.center[1], c=colors[idx], marker='x')
        for x in cluster.data:
            # plot data
            plt.scatter(x[0], x[1], c=colors[idx])

            if x in points_for_info:
                print_point_info(x, cluster, idx)

    plt.xlabel('income')
    plt.ylabel('infant')
    plt.show()

    # optimal k
    # plt.figure()
    # sum_squared_errors = []
    # for n_clusters in range(2, 10):
    #     kmeans = KMeans(n_clusters=n_clusters, max_iter=100)
    #     kmeans.fit(data)
    #     sse = kmeans.sum_squared_error()
    #     sum_squared_errors.append(sse)

    # plt.plot(sum_squared_errors)
    # plt.xlabel('# of clusters')
    # plt.ylabel('SSE')
    # plt.show()
