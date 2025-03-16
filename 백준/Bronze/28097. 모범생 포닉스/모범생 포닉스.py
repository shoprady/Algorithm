n = int(input())
time = sum(map(int, input().split())) + 8 * (n - 1)
print(time // 24, time % 24)