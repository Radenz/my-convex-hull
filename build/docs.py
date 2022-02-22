import os
from os.path import basename

base = basename(os.getcwd())

if base == "build":
    os.chdir("..")

print("\033[38;5;14mGenerating package documentation...\033[0m")
cmd = [
    "pdoc3",
    "--html",
    "--force",
    "-o",
    "docs",
    "-c",
    "show_source_code=False",
    "myConvexHull"
]

os.system(" ".join(cmd))
