import sys
import re

try:
    limit = int(sys.argv[2])
    if len(sys.argv) != 3:
        print("ERROR")
        exit()
    reg = r"\w{" + str(limit + 1) + ",}"
    res = re.findall(reg, sys.argv[1])
    print(res)
except ValueError:
    print("ERROR")
    exit()
