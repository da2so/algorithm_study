import sys

N = int(sys.stdin.readline().rstrip())

result = []
for i in range(N):
    ox = list(sys.stdin.readline().rstrip())

    tmp_result = 0
    prev_result = 1
    for j in ox:
        if j == 'O':
            tmp_result += prev_result
            prev_result += 1
        elif j == 'X':
            prev_result = 1

    result.append(tmp_result)

[print(i_result) for i_result in result]