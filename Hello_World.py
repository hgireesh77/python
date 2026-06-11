import os
import sys

# sys.argv[0] is the script name itself, sys.argv[1] is the first argument passed
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "Default Guest"
print(f"Hello World....{name}")
