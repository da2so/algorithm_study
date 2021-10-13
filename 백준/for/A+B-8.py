import sys

N = int(input())

result = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    assert 1 <= A, B <= 1000

    result.append([A, B, A+B])


[print(f'Case #{idx+1}: {A} + {B} = {output}') for idx, (A,B, output) in enumerate(result)]
