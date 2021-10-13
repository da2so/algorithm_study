import sys


result = []
while True:
    A, B = map(int, sys.stdin.readline().rstrip().split())

    if A != 0 and B !=0:
        assert 1 <= A, B <= 10
        result.append(A+B)
        continue
    break

[print(output) for output in result]
