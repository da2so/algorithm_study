a = int(input())
b = int(input())

assert -1e3 <= a,b <= 1e3
assert a, b != 0


if a > 0:
    if b > 0:
        print(1)
    else:
        print(4)
else:
    if b > 0:
        print(2)
    else:
        print(3)