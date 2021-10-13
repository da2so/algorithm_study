from collections import Counter

input = str(input())

upper_input = input.upper()
count_repeat = Counter(upper_input).most_common()

prev_num = -1
for string, num_repeat in count_repeat:

    if prev_num < num_repeat:
        prev_num = num_repeat
        result = string
    elif prev_num == num_repeat:
        result = '?'
        break
    else:
        break
print(result)

