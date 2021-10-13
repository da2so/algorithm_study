import sys

N = int(input())
assert 0 <= N <= 99

match = N

result = 0
while True:
    match = str(match)

    if len(match) == 1:
        match = '0' + match
    assert len(match) == 2

    tmp0 = match[1]
    tmp1 = str(int(match[0]) + int(match[1]))
    if len(tmp1) == 2:
        tmp1 = tmp1[1]
    match = tmp0 + tmp1
    result += 1
    if int(match) == N:
        break

print(result)