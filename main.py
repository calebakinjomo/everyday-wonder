"""Everyday Wonder — make.fun one-line entry.

Prints one sentence of everyday wonder and writes it to entry.txt.
"""

import os

ENTRY = "The coil turned, the chocolate hung by one spin, and the machine seemed to be deciding whether to be kind."

print(ENTRY)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
