import os


def install_deps():
    print("\033[38;5;14mInstalling dependencies...\033[0m")
    cmd = [
        "pip",
        "install",
        "numpy",
        "scipy",
        "pandas",
        "matplotlib"
    ]

    os.system(" ".join(cmd))


if __name__ == "__main__":
    install_deps()
