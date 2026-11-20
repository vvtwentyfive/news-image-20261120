#!/usr/bin/env python3
"""news-image-20261120 v2 entrypoint.

Copies the pre-rendered front page (entry.png, 1024x1024, drawn with PIL
from verified 19-20 November 2026 news) to the grader output directory.
Standard library only. Deterministic: the output is a byte-for-byte copy
of the shipped image, verified by sha256 after writing.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not SOURCE.is_file():
        print(f"entry.png not found next to main.py ({SOURCE})", file=sys.stderr)
        return 1
    # Gate check, mirroring the competition rules: a PNG of at most 1 MiB.
    with open(SOURCE, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if SOURCE.stat().st_size > 1048576:
        print(f"entry.png exceeds 1 MiB ({SOURCE.stat().st_size} bytes)", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    src_hash = sha256(SOURCE)
    dst_hash = sha256(dest)
    if src_hash != dst_hash:
        print(f"copy verification failed: {src_hash} != {dst_hash}", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({dest.stat().st_size} bytes, sha256 {dst_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
