import math


def circle_area(r):
    return r * r * math.pi


def circle_circumference(r):
    return 2 * r * math.pi


r = float(input())
print(f'{circle_area(r):.6f} {circle_circumference(r):.6f}')
