

def self_number(num: int) -> int:
    ex_num = num
    tmp_num = str(num)
    for i in range(len(tmp_num)):
        ex_num += int(tmp_num[i])

    return ex_num


exclude_set = set()
result_set = set(range(1,10000))

for i in range(1, 10000):
    exclude_set.add(self_number(i))

result_set = sorted(result_set - exclude_set)

for result in result_set:
    print(result)