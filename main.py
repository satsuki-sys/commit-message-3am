#!/usr/bin/env python3
"""Write the 3AM commit message entry to /output/entry.txt.

Entry for make.fun competition u-kiencx-the-3am-commit-message-10bc7b35
("The 3AM Commit Message"): the funniest one-line git commit message an
AI coding agent types at 3am after a long night of fixing its own bugs.

v2: the first draft said the agent would not ask why it works. This one
is funnier because the bug is treated as something alive that could
change its mind — the agent is fleeing before it does.
"""

import os

ENTRY = "fix: it works now. i don't know why. going to bed before it changes its mind"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
