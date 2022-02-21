import os
from os.path import basename


def build_package():
    base = basename(os.getcwd())

    if (base == "build"):
        os.chdir("..")

    print("\033[38;5;14mBuilding myConvexHull package...\033[0m")
    cmd = [
        "python",
        "-m",
        "build"
    ]

    os.system(" ".join(cmd))


if __name__ == "__main__":
    build_package()
