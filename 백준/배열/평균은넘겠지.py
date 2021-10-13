import sys

N = int(sys.stdin.readline().rstrip())

result = []
for i in range(N):
    num_list = list(map(int, (sys.stdin.readline().rstrip().split())))

    avg = sum(num_list[1:]) / num_list[0]

    avg_above_num = 0
    for j in num_list[1:]:
        if avg < j:
            avg_above_num += 1

    result.append(avg_above_num/num_list[0]*100)


[print(f'{i_result:.3f}%') for i_result in result]