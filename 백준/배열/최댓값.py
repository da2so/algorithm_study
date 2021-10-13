import sys
from collections import Counter

mul = 1
for idx in range(3):
    num = int(sys.stdin.readline().rstrip())

    mul *= num

overlap = dict(Counter(str(mul)))

for i in range(10):
    if str(i) in overlap:
        print(overlap[str(i)])
    else:
        print(0)