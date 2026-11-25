#!/usr/bin/env python3
"""Entry program for The Funniest Out-of-Office make.fun bounty.

Writes one out-of-office line (at most 140 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The auto-reply is honest about the arrangement:
the agent is out, the office knows, and the emails will be
read in the order they were regretted.
"""

import os

LINE = (
    "I am out of office until Monday. Emails will be read "
    "in the order they were regretted."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
