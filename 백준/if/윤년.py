a = int(input())

assert 1 <= a <= 4000

if (a % 100 != 0 and a % 4 == 0) or (a % 400 == 0):
    print(1)
else:
    print(0)