import numpy as np


class NumPyCreator:
    def from_list(lst, dtype=None):
        return np.array(lst, dtype=dtype)

    def from_tuple(tpl, dtype=None):
        return np.array(tpl, dtype=dtype)

    def from_iterable(itr, dtype=None):
        return np.array(itr, dtype=dtype)

    def from_shape(shape, value=0, dtype=None):
        return value * np.ones(shape=shape, dtype=None)

    def random(shape):
        return np.random.random_sample(size=shape)

    def identity(n, dtype=None):
        return np.identity(n=n, dtype=dtype)

