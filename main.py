#!/usr/bin/env python3
"""news-image-20261117: write one image summing up the world's news of
Tuesday 17 November 2026 to /output/entry.png.

The picture is a classic newspaper front page (entry.png, bundled with
this program): a globe icon + "THE WORLD'S NEWS" masthead + a dark-blue
nav bar, 10 main story cards (Ukraine's Kerch Bridge strike, Trump's
Quad summit in Manila, the US chip-export loophole, the fourth Hormuz
tanker fire, five EU states' Rwanda deportation plan, the West urging
Israel to open Gaza crossings, Depardieu admitting sex assault, Japan
scrambling jets, the Houthi advance in Yemen, Nvidia's earnings after
Huang's exit), each with a numbered tag + category ribbon + image +
headline + explainer, plus 32 more stories in the "ALSO ON TUESDAY"
list in 3 columns — 42 stories in total, all reported on Tuesday
17 November 2026 — and a world-landmarks skyline strip at the bottom.
The program copies it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png
and verifies the size and format.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    assert size <= 1_048_576, f"entry.png too large: {size} bytes (limit 1 MiB)"
    with open(dst, "rb") as fh:
        magic = fh.read(3)
    assert magic in (b"\xff\xd8\xff", b"\x89PN"), "entry.png is not a JPEG or PNG"
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
