a, b = map(int, input().split())

assert -1e4 <= a,b <= 1e4

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('==')