#!/usr/bin/env python3
"""news-image-20261120: copy the front-page image to the output directory.

Standard library only. The entry image (entry.png) sits beside this file;
running this script copies it to MAKEFUN_OUTPUT_DIR (default /output)
as entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
