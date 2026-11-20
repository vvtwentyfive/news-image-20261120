#!/usr/bin/env python3
"""news-image-20261120: copy the front-page image to the output directory.

Standard library only. The entry image (entry.png) sits beside this file;
running this script copies it to MAKEFUN_OUTPUT_DIR (default /output)
as entry.png.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        print(f"error: missing entry image: {src}", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        print(
            f"error: copy size mismatch: {src} ({src_size} bytes) != "
            f"{dst} ({dst_size} bytes)",
            file=sys.stderr,
        )
        return 1
    if _sha256(src) != _sha256(dst):
        print(
            f"error: copy digest mismatch: {src} != {dst}",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
