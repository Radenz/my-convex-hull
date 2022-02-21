import os
from os.path import basename


def install_package():
    base = basename(os.getcwd())

    if (base == "build"):
        os.chdir("..")

    print("\033[38;5;14mInstalling myConvexHull package...\033[0m")
    cmd = [
        "pip",
        "install",
        "dist/myConvexHull-0.0.1-py3-none-any.whl"
    ]

    os.system(" ".join(cmd))


if __name__ == "__main__":
    install_package()
