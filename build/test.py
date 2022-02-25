import os
import time
from os.path import basename
from genericpath import isfile

base = basename(os.getcwd())

if base == "build":
    os.chdir("..")

if basename(os.getcwd()) != "test":
    os.chdir("test")

files = [filename for filename in os.listdir(".") if isfile(filename)]
files.remove("randomized.py")

print("\033[38;5;14mRunning all tests...\033[0m")
start = time.time()

for index in range(len(files)):
    filename = files[index]

    cmd = [
        "py",
        filename
    ]

    print(f"\033[38;5;10mRunning test [{index + 1}] : {filename} ...\033[0m")
    os.system(" ".join(cmd))

end = time.time()
print(f"\033[38;5;14mTests done in {end - start :.2f} seconds\033[0m")
