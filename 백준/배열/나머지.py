import sys

st = 42

result = set()
for idx in range(10):
    num = int(sys.stdin.readline().rstrip())

    num = num % st
    result.add(num)

print(len(result))