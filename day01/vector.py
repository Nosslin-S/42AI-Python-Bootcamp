class Vector(list):
    # def __init__(self, vec: list):

    def __add__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("Only vectors can be added")
        else:
            add_vector = []
            for i in range(len(self)):
                add_vector.append(self[i] + vector[i])
            return add_vector

    def __radd__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("Only vectors can be added")
        else:
            return self + vector

    def __sub__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("Only vectors can be sbustracted")
        else:
            sub_vector = []
            for i in range(len(self)):
                sub_vector.append(self[i] - vector[i])
            return sub_vector

    def __rsub__(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError("Only vectors can be added")
        else:
            return self - vector

    def __truediv__(self, scalar):
        if not (isinstance(scalar, int) or isinstance(scalar, float)):
            raise TypeError("Only a scalar can divid a vector")
        else:
            div_vector = []
            for i in range(len(self)):
                div_vector.append(self[i] / scalar)
            return div_vector

    def __rtruediv__(self, scalar):
        return self / scalar

    def __mul__(self, vector):
        mul_vec = []
        if isinstance(vector, int) or isinstance(vector, float):
            for i in range(len(self)):
                mul_vec.append(self[i] * vector)
            return mul_vec
        elif isinstance(vector, Vector):
            for i in range(len(self)):
                mul_vec.append(self[i] * vector[i])
            return sum(mul_vec)
        else:
            raise TypeError("Only vectors or scalars can be multiplied together")

    def __rmul__(self, vector):
        return self * vector

    def __repr__(self):
        vector = []
        for i in range(len(self)):
            vector.append(self[i])
        return f"Vector {vector}"

    def __str__(self):
        return self.__repr__()
