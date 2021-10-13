N = int(input())

assert 1 <= N <= 1e4

result = 0

for i in range(1,N+1): result += i

print(result)