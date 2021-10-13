

N = int(input())
def arithmetic_sequence(num: int) -> bool:

    str_num = str(num)
    a_1 = str_num[0]

    sequence = str_num[1:]

    prev_d =0
    for idx in range(len(sequence)):
        d = (int(sequence[idx]) - int(a_1)) / (idx+1)
        if d != prev_d and idx >= 1:
            return 0
        prev_d = d
    return 1
result = 0
for i in range(1,N+1):
    result += arithmetic_sequence(i)

print(result)