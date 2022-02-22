import numpy as np
import matplotlib.pyplot as plt
import argparse
from myConvexHull import convex_hull
from myConvexHull.point_utils import X, Y


def random_color():
    r = hex(np.random.randint(0, 256))[2:]
    g = hex(np.random.randint(0, 256))[2:]
    b = hex(np.random.randint(0, 256))[2:]
    if len(r) == 1:
        r = "0" + r
    if len(g) == 1:
        g = "0" + g
    if len(b) == 1:
        b = "0" + b
    return f"#{r}{g}{b}"


parser = argparse.ArgumentParser()
parser.add_argument("cfgs", nargs=argparse.REMAINDER)

args = parser.parse_args()

configs = []
cfgs = args.cfgs

if len(cfgs) == 0:
    configs.append([-50, 0, 15])
    configs.append([-25, 25, 15])
    configs.append([0, 50, 15])

for config in cfgs:
    config = eval(config)
    if type(config) != list:
        raise f"Incorrect argument format : {config}"
    if len(config) != 3:
        raise f"Incorrect argument format : {config}"
    if type(config[0]) != int and type(config[1]) != int and type(config[2]) != int:
        raise f"Incorrect argument format : {config}"

    configs.append(config)

for config in configs:
    points = np.random.randint(config[0], config[1], [config[2], 2])
    hull = convex_hull(points)
    points = np.transpose(points)
    hull = np.transpose(hull)

    color = random_color()

    plt.scatter(points[X], points[Y], color=color)
    plt.plot(hull[X], hull[Y], color=color)

plt.show()
