import sys

num_list = []
N = int(sys.stdin.readline().rstrip())

num_list = list(map(int, (sys.stdin.readline().rstrip().split())))


max_val = max(num_list)

result = 0
for i in num_list:
    result += (i/max_val) * 100


print(f'{result / N}')