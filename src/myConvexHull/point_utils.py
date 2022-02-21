from myConvexHull.dtype import Point

Y = 1
X = 0


def less_than(a, b):
    # type: (Point, Point) -> bool
    return a[X] < b[X] or (a[X] == b[X] and a[Y] < b[Y])


def greater_than(a, b):
    # type: (Point, Point) -> bool
    return a[X] > b[X] or (a[X] == b[X] and a[Y] > b[Y])
