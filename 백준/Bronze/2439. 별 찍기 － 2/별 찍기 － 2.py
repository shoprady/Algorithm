N = int(input())
for i in range(1, N + 1):
    space = " " * (N - i)
    asterisk = "*" * i
    print(space + asterisk)