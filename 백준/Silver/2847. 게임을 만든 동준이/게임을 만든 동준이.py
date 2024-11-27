n = int(input())
levels = []
for _ in range(n):
    levels.append(int(input()))
    
ans = 0
for i in range(len(levels) - 1, 0, -1):
    if levels[i] <= levels[i-1]:
        diff = levels[i-1] - levels[i] + 1
        levels[i-1] -= diff
        ans += diff
print(ans)