"""
This modules provides basic utility functions regarding lines and
points, including helper functions that is used in the main
module, lines and points operations, etc.
"""
from myConvexHull.dtype import Point, Points, Line
from myConvexHull.point_utils import X, Y, distance
import numpy as np


def get_upper_points(points, line) -> Points:
    # type: (Points, Line) -> Points
    """
    Gets a subset of points which lies over a given line.

    Args:

    `points`: an array of points to get the subset of points of

    `line`: the line which the subset of points is over

    Returns:

    An array of points which lies over the specified line.
    """
    upper_points = np.ndarray([0, 2])
    for point in points:
        if _is_above_line(point, line):
            upper_points = np.append(upper_points, [point], axis=0)
    return upper_points


def get_lower_points(points, line) -> Points:
    # type: (Points, Line) -> Points
    """
    Gets a subset of points which lies under a given line.

    Args:

    `points`: an array of points to get the subset of points of

    `line`: the line which the subset of points is under

    Returns:

    An array of points which lies under the specified line.
    """
    lower_points = np.ndarray([0, 2])
    for point in points:
        if _is_below_line(point, line):
            lower_points = np.append(lower_points, [point], axis=0)
    return lower_points


def get_farthest_point(points, line) -> Point:
    # type: (Points, Line) -> Point
    """
    Gets the farthest point of a given line from a given set
    of points.

    Args:

    `points`: an array of points to get the subset of points of

    `line`: the line which the farthest point distance is
            calculated from

    Returns:

    An point which has the maximum distance of the specified
    line.
    """
    farthest_point = points[0]
    farthest_distance = _distance(farthest_point, line)
    index = 0
    for i in range(len(points)):
        point = points[i]
        dist = _distance(point, line)
        if dist > farthest_distance or (
            dist == farthest_distance and
            distance(point, _midpoint(line)) <
            distance(farthest_point, _midpoint(line))
        ):
            farthest_distance = dist
            farthest_point = point
            index = i
    return (farthest_point, index)


def is_vertical(line) -> bool:
    # type: (Line) -> bool
    """
    Checks if a given line is vertical or not.

    Args:

    `line`: the line to check

    Returns:

    `True` if the given line is vertical, `False` otherwise.
    """
    return line[0][X] == line[1][X]


def _is_above_line(point, line):
    # type: (Point, Line) -> bool
    """
    Checks if a specific point is above a given line.

    Args:

    `point`: the point to check

    `line`: the given line

    Returns:

    `True` if the point is above the line, `False` otherwise.
    """
    slope = _slope(line[0], line[1])
    offset = _offset(line[0], slope)
    return point[Y] - slope * point[X] > offset


def _is_below_line(point, line):
    # type: (Point, Line) -> bool
    """
    Checks if a specific point is below a given line.

    Args:

    `point`: the point to check

    `line`: the given line

    Returns:

    `True` if the point is below the line, `False` otherwise.
    """
    slope = _slope(line[0], line[1])
    offset = _offset(line[0], slope)
    return point[Y] - slope * point[X] < offset


def _slope(a: Point, b: Point) -> float:
    # type: (Point, Point) -> bool
    """
    Calculates the slope of a line passing through two given
    points.

    .. warning::
        Checks beforehand whether the line is vertical using
        `is_vertical` function, otherwise may throw an error
        if the slope is undefined (for vertical line).

    Args:

    `a`: the first point that the line passes through

    `b`: the second point that the line passes through

    Returns:

    The slope of the line.
    """
    return (b[Y] - a[Y]) / (b[X] - a[X])


def _offset(a: Point, slope: float) -> float:
    # type: (Point, float) -> float
    """
    Calculates the y-offset from the origin of a line passing
    through a point with a given slope.

    Args:

    `a`: the point that the line passes through

    `slope`: the slope of the line

    Returns:

    The y-offset of the line from the origin.
    """
    return a[1] - slope * a[0]


def _distance(point, line):
    # type: (Point, Line) -> float
    """
    Calculates the distance between a point and a line.

    Args:

    `point`: the point to calculate the distance of

    `line`: the point to calculate the distance of

    Returns:

    The distance between the specified point and line.
    """
    _point = np.array(point)
    a = np.array(line[0])
    b = np.array(line[1])
    return np.abs(np.cross(b - a, _point - a) / np.linalg.norm(b - a))


def _midpoint(line):
    # type: (Line) -> Point
    """
    Calculates the midpoint of a line.

    Args:

    `line`: the line to calculate the midpoint of

    Return:

    The midpoint of the line.
    """
    return (line[0] + line[1]) / 2
