import sys
n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
for i in range(1, n + 1):
    sums.append(sums[i - 1] + nums[i - 1])
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sums[j] - sums[i - 1])