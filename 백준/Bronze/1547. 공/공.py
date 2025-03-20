import sys
ball = 1
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    if ball == 1:
        if a == 1: ball = b
        elif b == 1: ball = a
    elif ball == 2:
        if a == 2: ball = b
        elif b == 2: ball = a
    else:
        if a == 3: ball = b
        elif b == 3: ball = a
print(ball)