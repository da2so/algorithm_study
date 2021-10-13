H, M = map(int, input().split())

assert 0 <= H <= 23
assert 0 <= M <= 59


minus = 45

if M < 45:
    H -= 1
    M += 15
    if H < 0:
        H = 23
else:
    M -= 45


print(H, M)
