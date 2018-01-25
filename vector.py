import numpy
from math import pi
# from decimal import Decimal, getcontext

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR = "Cannot normalize a zero vector!"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([x for x in coordinates])
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
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR)

    def dot_product(self, v):
        temp = Vector([x*y for x, y in zip(self.coordinates, v.coordinates)])
        return sum(temp.coordinates)

    def angle_with(self, w, in_degrees = False):
        try:
            uv = self.normalize()
            uw = w.normalize()
            vdotw = uv.dot_product(uw)
            angle_in_rad = numpy.arccos(vdotw)
            if in_degrees:
                deg_per_rad = 180. / pi
                return angle_in_rad * deg_per_rad
            else:
                return angle_in_rad
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                print("One of the vectors is a ZERO vector! Cant calc angle!")
            else:
                raise e
