import os


def uninstall_package():

    print("\033[38;5;14mUninstalling myConvexHull package...\033[0m")
    cmd = [
        "pip",
        "uninstall",
        "myConvexHull",
    ]

    os.system(" ".join(cmd))


if __name__ == "__main__":
    uninstall_package()
