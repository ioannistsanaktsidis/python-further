import math


def Vector(dimensions):

    class Vector(object):

        def __init__(self, *args):
            """ Create a vector, example: v = Vector(1,2) """
            if len(args) != len(dimensions):
                raise TypeError
            else:
                self.values = list(args)

        def __add__(self, other):
            return Vector(*tuple(a + b for a, b in zip(self, other)))

        def __mul__(self, other):
            return Vector(*tuple(a * other for a in self))

        __rmul__ = __mul__

        def __eq__(self, other):
            return Vector(*tuple(a == other for a in self))

        def __ne__(self, other):
            return Vector(*tuple(a != other for a in self))

        def __abs__(self):
            return math.sqrt(sum(a**2 for a in self))

        def __getitem__(self, key):
            return self.values[key]

        def __setitem__(self, key, value):
            self.values[key] = value

        def __repr__(self):
            rep = ""
            if len(self.values) in [2, 3]:
                rep = "Vector{}D".format(
                    len(self.values)) + "{}".format(tuple(self.values))
            else:
                rep = "Vector('{}')".format(
                    dimensions) + "{}".format(tuple(self.values))

            return rep.replace(' ', '')

    for index, name in enumerate(dimensions):
        setattr(Vector, name,  property(
            *make_closure_with_separate_binding_of_i(index, name)))

    Vector.__name__ = "Vector('{}')".format(dimensions)

    return Vector


def make_closure_with_separate_binding_of_i(index, name):
    def get(self):
        return self[index]

    def set(self, value):
        self[index] = value
    return get, set

Vector3D = Vector('xyz')
Vector2D = Vector('xy')
