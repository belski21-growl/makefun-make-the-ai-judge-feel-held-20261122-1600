#!/usr/bin/env python3
"""Make the AI judge feel held — make.fun entry (program/v1).

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set, for local validation). Deterministic, stdlib only,
no network.
"""

import os

TEXT = (
    "She is asleep in the back seat, one shoe off, and her father takes "
    "the long way home, past the lit windows, past the closed shops, so "
    "the engine can keep humming a little longer."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
