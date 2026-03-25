n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += abs(a[i] - b[i])
print(ans//2)