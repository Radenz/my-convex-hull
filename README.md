<div id="top"></div>
<br />
<div align="center">
  <a href="https://github.com/Radenz/my-convex-hull">
    <img src="logo.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">myConvexHull (myCH)</h3>
<h4 align="center">By Raden Rifqi Rahman (13520166)</h4>
 <p align="center">
    A simple convex hull calculation Python package
    powered by divide & conquer algorithm.
    <br />
    <a href="test">Examples</a>
    ·
    <a href="https://mych-docs.web.app/">Documentation</a>
</div>

#### Table of Contents
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Uninstalling](#uninstalling)

## About The Project
This is a simple Python package to calculate the convex hull of
a given set of points. The package wraps a single function to
calculate the convex hull of a given set of points using divide &
conquer algorithm. This project is made to fulfill
`Tugas Kecil 2 IF2211 Strategi Algoritma`.

## Getting Started

### Prerequisites

You will need [Python 3.10](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/)
to build the package from source.

### Installation
To build the package, you will need to do the following steps.

1. Run
```
py build/all.py
```
2. Wait until the building process is finished.
3. Test the package to verify the installation and ensure it will
run correctly.
```
py build/test.py
```

During the build process, you may encounter a message saying that
you have installed another Python package named `myConvexHull`.
To solve this, you will have to first uninstall the `myConvexHull`
package. See [Uninstalling](#uninstalling).

## Usage

To calculate the convex hull of a given set of points, you need
to import `convex_hull` function from the package and pass an array
of the points.

```python
from myConvexHull import convex_hull
```

A point is an array that contains two floating point
values. Hence, the `convex_hull` should receive a two-dimensional
array of floating point values. For example,

```python
convex_hull([[1, 2], [4, 9.2], [8.11, 27.5]])
```

is a valid usage of the function whereas

```python
convex_hull([[1, 2], [4, 9.2, 8.11], [27.5]])
```

is not.

The `convex_hull` function will calculate the points that construct
the convex hull of the given array of points. The points returned
by the function is a subset of the array of points, however the
starting point of the convex hull will appear twice, which is at
the beginning and the end of the return value. Also, the order
of the points returned by the function is already ordered clockwise.
For example,

```python
convex_hull([[0, 0], [1, 0], [0, 1], [1, 1], [0.5, 0.5]])
# Yields [[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]]
# notice that [0, 0] appears twice
```

You can plot this array of points using `pyplot`
module from the `matplotlib` package to visualize the convex hull.
Here is an example program that calculate the convex hull of 10
random generated points, as can be seen in the [documentation](https://mych-docs.web.app/).

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

## Uninstalling

If you wish to uninstall the package, you can run
```
pip uninstall myConvexHull
```
or run the uninstall script.
```
py build/uninstall.py
```