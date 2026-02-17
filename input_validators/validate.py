
import sys
import re
line = sys.stdin.readline()

if not re.match(r"[0-9]+ [0-9]+", line):
    print(f"regex failing", file=sys.stderr)
    sys.exit(43)


if sys.stdin.readline() != "":
    sys.exit(43)


sys.exit(42)
