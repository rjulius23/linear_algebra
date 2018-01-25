from vector import Vector as V
import numpy


if __name__ == "__main__":
    v1 = V([7.887, 4.138])
    w1 = V([-8.802, 6.776])

    v2 = V([3.183, -7.627])
    w2 = V([-2.668, 5.319])

    v3 = V([-5.955, -4.904, -1.874])
    w3 = V([-4.496, -8.755, 7.103])

    v4 = V([7.35, 0.221, 5.188])
    w4 = V([2.751, 8.259, 3.985])

    print(v1.dot_product(w1))
    print(v2.angle_with(w2))

    print(v3.dot_product(w3))
    print(v4.angle_with(w4, True))
