from typing import TypeAlias, Any
import numpy as np
import numpy.typing as npt

Point: TypeAlias = npt.NDArray
Points: TypeAlias = npt.NDArray
Line: TypeAlias = tuple[npt.NDArray, npt.NDArray]
NullableLine: TypeAlias = Line | None