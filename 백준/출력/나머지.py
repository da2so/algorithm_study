
a, b, c = map(int, input().split())

assert 2 <= a, b <= 10000
assert 2 <= c <= 10000

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)


