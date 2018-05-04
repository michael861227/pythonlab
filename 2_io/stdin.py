import sys

def readlines():
    for line in sys.stdin: #用sys內的stdin
        line = line.strip()
        num = int(line)
        print(num+1)

readlines()