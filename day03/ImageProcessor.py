import matplotlib.pyplot as plt
import os
import numpy as np


class ImageProcessor:
    def load(path):
        if os.path.exists(path) and os.path.isfile(path):
            img = plt.imread(path)
            print(
                "Loading image of dimensions {} x {}".format(img.shape[0], img.shape[1])
            )
            return img
        else:
            print("The path does not exist")
            return None

    def display(array):
        if isinstance(array, np.ndarray):
            plt.imshow(array)
        else:
            raise TypeError("The array must be a numpy array")
