N = int(input())

result = []
for i in range(N):
    A, B = map(int, input().split())
    assert 1 <= A, B <= 9

    result.append(A+B)

[print(output) for output in result]
