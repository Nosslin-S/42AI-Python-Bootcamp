import numpy as np


class ColorFilter:
    def invert(array):
        return 1 - array

    def to_blue(array):
        tmp_arr = np.zeros(array.shape)
        tmp_arr[:, :, 2] = array[:, :, 2]
        return tmp_arr

    def to_green(array):
        tmp_arr = array * 0
        tmp_arr[:, :, 1] = array[:, :, 1]
        return tmp_arr

    def to_red(array):
        return array - ColorFilter.to_blue(array) - ColorFilter.to_green(array)

    def to_grayscale(array, filter="weighted"):
        if filter == "m" or filter == "mean":
            for color_array in array:
                for rgb in color_array:
                    rgb[:] = np.mean(rgb[:])
            return array
        elif filter == "w" or filter == "weighted":
            for color_array in array:
                for rgb in color_array:
                    rgb[:] = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
            return array
