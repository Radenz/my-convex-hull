import numpy as np
from point_utils import greater_than, less_than
from dtype import Points, NullableLine, Line, Point
from line import get_farthest_point, get_lower_points, get_upper_points
from enum import Enum


def convex_hull(points, base_line=None, direction=None):
    # type: (Points, NullableLine, Direction) -> Points

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
        new_points_a = func(points, new_base_line_a)
        new_points_b = func(points, new_base_line_b)

        chl = convex_hull(new_points_a, new_base_line_a, direction)
        chr = convex_hull(new_points_b, new_base_line_b, direction)

        hull = _merge(chl, farthest_point, chr, direction)
    else:
        (leftmost_point, lmindex) = _get_leftmost_point(points)
        (rightmost_point, rmindex) = _get_rightmost_point(
            points
        )

        points = np.delete(points, [lmindex, rmindex], axis=0)

        line: Line = (leftmost_point, rightmost_point)
        (upper_points, lower_points) = _split(points, line)

        chu = convex_hull(upper_points, line, Direction.UPWARDS)
        chl = convex_hull(lower_points, line, Direction.DOWNWARDS)
        hull = _first_merge(leftmost_point, chu, rightmost_point, chl)

    return hull


def _split(points, line):
    # type: (Points, Line) -> tuple[Points, Points]
    upper_points = get_upper_points(points, line)
    lower_points = get_lower_points(points, line)
    return (upper_points, lower_points)


def _first_merge(left_vertex, upper_vertices, right_vertex, lower_vertices):
    hull = np.ndarray([0, 2])
    hull = np.append(hull, [left_vertex], axis=0)
    hull = np.append(hull, upper_vertices, axis=0)
    hull = np.append(hull, [right_vertex], axis=0)
    hull = np.append(hull, lower_vertices, axis=0)
    hull = np.append(hull, [left_vertex], axis=0)
    return hull


def _merge(left_vertices, mid_vertex, right_vertices, direction):
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
    # type: (np.ndarray[np.ndarray]) -> np.ndarray
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
    UPWARDS = 0
    DOWNWARDS = 1
