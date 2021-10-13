
N = input()

num = int(input())

result = 0
for i in range(len(str(num))):
    result += int(str(num)[i])

print(result)