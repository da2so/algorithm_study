
a = int(input())
b = int(input())

assert len(str(a)) == 3
assert len(str(b)) == 3

print(a * int(str(b)[2]))
print(a * int(str(b)[1]))
print(a * int(str(b)[0]))
print(a * b)