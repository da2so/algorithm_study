import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
assert 1 <= N, X <= 1e4

result = []
num_list = map(int, sys.stdin.readline().rstrip().split())

for i_num in num_list:
    assert 1 <= i_num <= 1e4
    if i_num < X:
        result.append(i_num)

[print(output, end=' ') for output in result]
