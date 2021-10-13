import sys

N = int(input())

result = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    assert 1 <= A, B <= 1000

    result.append(A+B)


[print(output) for output in result]
