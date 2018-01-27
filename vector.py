import numpy
import math
from math import pi
from decimal import Decimal, getcontext


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR = "Cannot normalized a zero vector!"
    NO_UNIQUE_PARALLEL_COMPONENT = "No unique parallel component of this vector!"
    NO_UNIQUE_ORTHOGONAL_COMPONENT = "No unique orthogonal component of this vector!"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            # TODO: Introduce tolerance instead of rounding the values as this is
            # a limitation for now
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])

    def __mul__(self, scalar):
        return Vector([Decimal(scalar) * x for x in self.coordinates])

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        sum_m = Decimal(numpy.sum([x * x for x in self.coordinates]))
        magnitude = Decimal(numpy.sqrt(sum_m))
        return magnitude

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return Decimal('1.0')/magnitude * self
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR)

    def dot_product(self, v):
        temp = Vector([x*y for x, y in zip(self.coordinates, v.coordinates)])
        return numpy.sum(temp.coordinates)

    def angle_with(self, w, in_degrees=False):
        try:
            uv = self.normalized()
            uw = w.normalized()
            vdotw = uv.dot_product(uw)
            # numpy.arccos didnt work with Decimal, so changed to math.acos
            angle_in_rad = math.acos(vdotw)
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

    # TODO: Introudce tolerance
    def is_parallel(self, w):
        if self.dimension != w.dimension:
            return False
        for i in range(self.dimension):
            # Case of different values
            if self.coordinates[i] != 0 and w.coordinates[i] != 0:
                scalar = self.coordinates[i] / w.coordinates[i]
                if scalar * w == self:
                    return True
                else:
                    return False
            # Case if one of them is a zero vector
            elif self.magnitude() == 0 or w.magnitude() == 0:
                return True
            else:
                continue

        return False

    def is_orthogonal(self, w):
        if self.dimension != w.dimension:
            return False
        if self.dot_product(w) == 0:
            return True
        else:
            return False

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            dotp = self.dot_product(u)
            return dotp * u
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT)
            else:
                raise e
    
    def component_orthogonal_to(self, basis):
        try:
            return self - self.component_parallel_to(basis)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT)
            else:
                raise e
