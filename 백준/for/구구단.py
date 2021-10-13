N = int(input())

assert 1 <= N <= 9

[print (f'{N} * {i} = {N*i}') for i in range(1,10)]