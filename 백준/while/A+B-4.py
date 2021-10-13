import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())
        assert 1 <= A, B <= 10
        print(A+B)
    except:
        break




