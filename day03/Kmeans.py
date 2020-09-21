import numpy as np


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        None.
        Raises:
        This function should not raise any Exception.
        """
        counter = 0
        # Generate the initial centroids
        if self.centroids == []:

            for _ in range(self.ncentroid):
                self.centroids.append(
                    (
                        np.random.uniform(min(X[:, 0]), max(X[:, 0])),
                        np.random.uniform(min(X[:, 1]), max(X[:, 1])),
                        np.random.uniform(min(X[:, 2]), max(X[:, 2])),
                    )
                )

        while counter < self.max_iter:
            prediction = self.predict(X)
            for i in range(self.ncentroid):
                filtered_points = X[prediction == i]
                self.centroids[i] = (
                    np.mean(filtered_points[:, 0]),
                    np.mean(filtered_points[:, 1]),
                    np.mean(filtered_points[:, 2]),
                )
            counter += 1
        return None

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        the prediction as a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        This function should not raise any Exception.
        """
        dist_matrix = np.zeros((X.shape[0], self.ncentroid))
        for i in range(self.ncentroid):
            dist_matrix[:, i] = np.linalg.norm(X - self.centroids[i], axis=1)

        return np.argmin(dist_matrix, axis=1)


X = np.genfromtxt("solar_system_census.csv", delimiter=",")
X = X[1:, 1:]
algo = KmeansClustering()
algo.fit(X)
for centroid in algo.centroids:
    print(centroid)

