"""Write the competition entry: two lines to your past self.

Line 1 warns your past self about one specific moment in a single
sentence; line 2 says in one sentence why that moment mattered and
what changed because of it.
"""

import os

ENTRY = (
    "Do not approve the Friday-night deploy on 13 November, because the migration script silently drops the users table.\n"
    "That one click cost us the weekend, the client, and every record we could never rebuild."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
