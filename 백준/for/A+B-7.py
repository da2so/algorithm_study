import sys

result = []
while True:
    A, B = map(int, sys.stdin.readline().rstrip().split())
    assert 1 <= A, B <= 10

    if A != 0 and B !=0:
        result.append(A+B)
        continue
    break

