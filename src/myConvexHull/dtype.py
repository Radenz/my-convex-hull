"""
This module provides type hints used by the other modules.
"""
from typing import TypeAlias
import numpy.typing as npt

Point: TypeAlias = npt.NDArray
Points: TypeAlias = npt.NDArray
Line: TypeAlias = tuple[npt.NDArray, npt.NDArray]
NullableLine: TypeAlias = Line | None

__pdoc__ = {}
__pdoc__["Point"] = "Point type. An array of two floating point values."
__pdoc__["Points"] = "Points type. An array of Points."
__pdoc__["Line"] = "Line type. An tuple containing exactly two points."
__pdoc__["NullableLine"] = "NullableLine type. A Line type which value can be None."
