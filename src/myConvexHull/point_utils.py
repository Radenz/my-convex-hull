"""
This module provides basic utilities related to Point type,
such as comparison function between two points.
"""
import numpy as np
from myConvexHull.dtype import Point

Y = 1
"A constant index to access the y value of a point."
X = 0
"A constant index to access the x value of a point."


def less_than(a, b) -> bool:
    # type: (Point, Point) -> bool
    """
    Compares two points and returns true if the first point's
    x value is less than the second point's x value or both
    points have the same x value but the first point's y value
    is less than the second point's y value.

    Args:

    `a`: the first `Point`

    `b`: the second `Point`

    Return:

    `True` if the true condition is met, `False` otherwise.
    """
    return a[X] < b[X] or (a[X] == b[X] and a[Y] < b[Y])


def greater_than(a, b) -> bool:
    # type: (Point, Point) -> bool
    """
    Compares two points and returns true if the first point's
    x value is more than the second point's x value or both
    points have the same x value but the first point's y value
    is more than the second point's y value.

    Args:

    `a`: the first `Point`

    `b`: the second `Point`

    Return:

    `True` if the true condition is met, `False` otherwise.
    """
    return a[X] > b[X] or (a[X] == b[X] and a[Y] > b[Y])


def distance(a, b) -> float:
    # type: (Point, Point) -> bool
    """
    Calculates the distance between two points.

    Args:

    `a`: the first `Point`

    `b`: the second `Point`

    Return:

    The distance between the specified points.
    """
    return np.sqrt((a[X] - b[X]) ** 2 + (a[Y] - b[Y]) ** 2)
