import numpy


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([numpy.subtract(self.coordinates, v.coordinates)])

    def __mul__(self, scalar):
        return Vector([scalar * x for x in self.coordinates])

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return numpy.round(numpy.sqrt(numpy.sum([x*x for x in self.coordinates])),3)

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return 1./magnitude * self
        except ZeroDivisionError:
            print("Cannot divide ZERO vector!!!")