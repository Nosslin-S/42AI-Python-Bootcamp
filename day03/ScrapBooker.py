import numpy as np


class ScrapBooker:
    def crop(array, dimensions, position=(0, 0)):
        if (
            dimensions[0] + position[0] > array.shape[0]
            or dimensions[1] + position[1] > array.shape[1]
        ):
            raise ValueError(
                "The croping dimensions cannot be bigger than the picture's dimensions"
            )
        else:
            return array[
                position[0] : position[0] + dimensions[0],
                position[1] : position[1] + dimensions[1],
            ]

    def thin(array, n, axis=0):
        return np.delete(array, list(range(n, array.shape[axis], n)), axis=axis)

    def juxtapose(array, n, axis=0):
        if n == 0:
            return array
        array_jux = np.concatenate((array, array), axis=axis)
        while n > 1:
            array_jux = np.concatenate((array_jux, array), axis=axis)
            n -= 1
        return array_jux

    def mosaic(array, dimensions):
        array_0 = ScrapBooker.juxtapose(array, dimensions[0], 0)
        return ScrapBooker.juxtapose(array_0, dimensions[1], 1)

