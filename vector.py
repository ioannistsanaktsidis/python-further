import math
import operator


class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _o2(self, other, f):
        "Any two-operator operation where the left operand is a Vector"
        if isinstance(other, Vector):
            return Vector(f(self.x, other.x),
                          f(self.y, other.y))
        elif (hasattr(other, "__getitem__")):
            return Vector(f(self.x, other[0]),
                          f(self.y, other[1]))
        else:
            return Vector(f(self.x, other),
                          f(self.y, other))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        if (hasattr(other, "__getitem__")):
            return Vector(self.x * other[0], self.y * other[1])
        else:
            return Vector(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __div__(self, other):
        return self._o2(other, operator.div)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vector")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError("Invalid subscript " + str(key) + " to Vector")

    def __iter__(self):
        return self.values.__iter__()

    def __neg__(self):
        return Vector(operator.neg(self.x), operator.neg(self.y))

    def __pos__(self):
        return Vector(operator.pos(self.x), operator.pos(self.y))

    def __invert__(self):
        return Vector(-self.x, -self.y)
