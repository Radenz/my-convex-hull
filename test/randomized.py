import numpy as np
import matplotlib.pyplot as plt
import argparse
from myConvexHull import convex_hull, random_color
from myConvexHull.point_utils import X, Y


def throw():
    print(f"Incorrect argument format : {config}")
    print(f"Usage: [config [config [config [...]]]]")
    print()
    print(f"\tconfig\t\"[<x-min>, <x-max>, <y-min>, <y-max>, <count>]\"")
    print(f"\texample: \"[-50, 0, -50, -25, 15]\"")
    print()
    exit(1)


parser = argparse.ArgumentParser()
parser.add_argument("cfgs", nargs=argparse.REMAINDER)

args = parser.parse_args()

configs = []
cfgs = args.cfgs

if len(cfgs) == 0:
    configs.append([-50, 0, -50, -25, 15])
    configs.append([-25, 25, -10, 10, 15])
    configs.append([0, 50, 25, 50, 15])


for config in cfgs:
    try:
        config = eval(config)
    except:
        throw()
    if type(config) != list:
        throw()
    if len(config) != 5:
        throw()

    for i in range(5):
        if type(config[i]) != int:
            throw()

    configs.append(config)

plt.title('Randomized Testing')
plt.xlabel("x")
plt.ylabel("y")

for config in configs:
    x = np.random.randint(config[0], config[1], [config[4], 1])
    y = np.random.randint(config[2], config[3], [config[4], 1])
    points = x
    points = np.append(points, y, axis=1)
    hull = convex_hull(points)
    points = np.transpose(points)
    hull = np.transpose(hull)

    color = random_color()

    plt.scatter(points[X], points[Y], color=color)
    plt.plot(hull[X], hull[Y], color=color)

plt.show()
