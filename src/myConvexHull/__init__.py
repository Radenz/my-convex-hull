"""
This package contains the main convex hull calculation function
to calculate the points of a convex hull from a given array of
points.
"""

import numpy as np
from myConvexHull.point_utils import *
from myConvexHull.dtype import *
from myConvexHull.line_utils import *
from enum import Enum


def convex_hull(points, base_line=None, direction=None) -> Points:
    # type: (Points, NullableLine, Direction) -> Points
    """
    Calculates the set of points that construct the convex hull of
    the given array of points. The calculation is done using divide
    and conquer algorithm.

    Args:

    `points`: an array of points to calculate the convex hull of

    `base_line`: the base line of previous iteration convex hull points

    `direction`: the direction of which the points of the convex hull is
                 expanding

    Returns:

    An array of points that construct the convex hull of the given array
    of points.

    Example usage:

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from myConvexHull import convex_hull
    from myConvexHull.point_utils import X, Y
    points = np.random.randint(-30, 30, [10, 2])
    hull = convex_hull(points)
    points = np.transpose(points)
    hull = np.transpose(hull)
    plt.scatter(points[X], points[Y])
    plt.plot(hull[X], hull[Y])
    plt.show()
    ```
    """

    if base_line:
        if len(points) == 0:
            return np.ndarray([0, 2])
        if len(points) == 1:
            return points

        (farthest_point, index) = get_farthest_point(points, base_line)
        points = np.delete(points, [index], axis=0)

        new_base_line_a = (base_line[0], farthest_point)
        new_base_line_b = (farthest_point, base_line[1])

        func = get_upper_points if direction == Direction.UPWARDS else get_lower_points

        # Guard
        if is_vertical(new_base_line_a):
            chl = np.ndarray([0, 2])
        else:
            new_points_a = func(points, new_base_line_a)
            chl = convex_hull(new_points_a, new_base_line_a, direction)

        # Guard
        if is_vertical(new_base_line_b):
            chr = np.ndarray([0, 2])
        else:
            new_points_b = func(points, new_base_line_b)
            chr = convex_hull(new_points_b, new_base_line_b, direction)

        hull = merge(chl, farthest_point, chr, direction)
    else:
        (leftmost_point, lmindex) = _get_leftmost_point(points)
        (rightmost_point, rmindex) = _get_rightmost_point(
            points
        )

        points = np.delete(points, [lmindex, rmindex], axis=0)

        line: Line = (leftmost_point, rightmost_point)

        # Guard
        if is_vertical(line):
            upper_points = np.ndarray([0, 2])
            lower_points = np.ndarray([0, 2])
        else:
            (upper_points, lower_points) = split(points, line)

        chu = convex_hull(upper_points, line, Direction.UPWARDS)
        chl = convex_hull(lower_points, line, Direction.DOWNWARDS)
        hull = first_merge(leftmost_point, chu, rightmost_point, chl)

    return hull


def split(points, line) -> tuple[Points, Points]:
    # type: (Points, Line) -> tuple[Points, Points]
    """
    Split a set of points into two sets of points separated
    by a line. The line is represented by a tuple of 2 points.

    Args:

    `points`: the set of points to split

    `line`: a tuple of 2 points representing a line on which
            splitting is based

    Returns:

    A tuple of two set of points separated by the line.
    """
    upper_points = get_upper_points(points, line)
    lower_points = get_lower_points(points, line)
    return (upper_points, lower_points)


def first_merge(left_vertex, upper_vertices, right_vertex, lower_vertices) -> Points:
    # type: (Point, Points, Point, Points) -> Points
    """
    Merge subsolution of upper points hull and lower points hull
    after splitted by the line through `left_vertex` and
    `right_vertex` in the first iteration.

    Args:

    `left_vertex`: the bottom-leftmost point which the line in the
                   the first iteration pass through

    `upper_vertices`: upper points hull

    `right_vertex`: the top-rightmost point which the line in the
                   the first iteration pass through

    `lower_vertices`: lower points hull

    Returns:

    An array of points which construct the convex hull.
    """
    hull = np.ndarray([0, 2])
    hull = np.append(hull, [left_vertex], axis=0)
    hull = np.append(hull, upper_vertices, axis=0)
    hull = np.append(hull, [right_vertex], axis=0)
    hull = np.append(hull, lower_vertices, axis=0)
    hull = np.append(hull, [left_vertex], axis=0)
    return hull


def merge(left_vertices, mid_vertex, right_vertices, direction) -> Points:
    # type: (Point, Points, Point, Points) -> Points
    """
    Merge subsolution of leftside points hull and rightside points hull
    after splitted by the line through the farthest point from the line
    of the previous iteration.

    Args:

    `left_vertices`: leftside points hull

    `mid_vertex`: the farthest point from the line of the previous
                  iteration

    `right_vertices`: rightside points hull

    `direction`: the direction which the hull is expanding

    Returns:

    An array of points which is the subset of points that
    construct the convex hull.
    """
    hull = np.ndarray([0, 2])
    if direction == Direction.UPWARDS:
        hull = np.append(hull, left_vertices, axis=0)
        hull = np.append(hull, [mid_vertex], axis=0)
        hull = np.append(hull, right_vertices, axis=0)
    else:
        hull = np.append(hull, right_vertices, axis=0)
        hull = np.append(hull, [mid_vertex], axis=0)
        hull = np.append(hull, left_vertices, axis=0)
    return hull


def _get_leftmost_point(points):
    # type: (Points) -> tuple[Point, int]
    """
    Gets the bottom-leftmost point and its index from a given
    set of points.

    Args:

    `points`: an array of points to get the bottom-leftmost of

    Returns:

    A tuple containing the bottom-leftmost point and its index.
    """
    if len(points) == 0:
        return None

    leftmost_point: Point = None
    index = 0
    for i in range(len(points)):
        point = points[i]
        if leftmost_point is None or less_than(point, leftmost_point):
            leftmost_point = point
            index = i

    return (leftmost_point, index)


def _get_rightmost_point(points):
    # type: (Points) -> tuple[Point, int]
    """
    Gets the top-rightmost point and its index from a given
    set of points.

    Args:

    `points`: an array of points to get the top-rightmost of

    Returns:

    A tuple containing the top-rightmost point and its index.
    """
    if len(points) == 0:
        return None

    rightmost_point: Point = None
    index = 0
    for i in range(len(points)):
        point = points[i]
        if rightmost_point is None or greater_than(point, rightmost_point):
            rightmost_point = point
            index = i

    return (rightmost_point, index)


class Direction(Enum):
    """
    Vertical direction enumerated values.
    """
    UPWARDS = 0
    "Upwards direction"
    DOWNWARDS = 1
    "Downwards direction"
