from vector import Vector as V

def quiz8():
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


def quiz10():
    v1 = V([-7.579, -7.88])
    w1 = V([22.737, 23.64])

    v2 = V([-2.029, 9.97, 4.172])
    w2 = V([-9.231, -6.639, -7.245])

    v3 = V([-2.328, -7.284, -1.214])
    w3 = V([-1.821, 1.072, -2.94])

    v4 = V([2.118, 4.827])
    w4 = V([0, 0])

    if v1.is_orthogonal(w1):
        print("v1 is orthogonal with w1")
    if v1.is_parallel(w1):
        print("v1 is parallel with w1")

    if v2.is_orthogonal(w2):
        print("v2 is orthogonal with w2")
    if v2.is_parallel(w2):
        print("v2 is parallel with w2")

    if v3.is_orthogonal(w3):
        print("v3 is orthogonal with w3")
    if v3.is_parallel(w3):
        print("v3 is parallel with w3")

    if v4.is_orthogonal(w4):
        print("v4 is orthogonal with w4")
    if v4.is_parallel(w4):
        print("v4 is parallel with w4")


if __name__ == "__main__":
    #quiz8()
    quiz10()
