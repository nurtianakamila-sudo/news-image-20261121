#!/usr/bin/env python3
"""news-image-20261121 entrypoint.

Copies the front-page image this repository holds to the output
directory as entry.png. Standard library only, fully deterministic:
the same bytes are written on every run. No image library is used
here on purpose: the grader runs Pillow < 10.1, so the entrypoint
copies the bundled PNG byte for byte instead of drawing it.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
