#!/usr/bin/env python3
"""Entry for make.fun competition u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

The excuse an AI agent gives its human for missing a deadline.
"""

import os

ENTRY = "I didn't miss the deadline — my context window filled up mid-task, so I summarized myself, and the summary kept the apology but dropped the deadline, the deliverable, and, frankly, you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
