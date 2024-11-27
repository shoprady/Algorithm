n = int(input())
levels = []
for _ in range(n):
    levels.append(int(input()))
    
def check_levels(levels):
    ans = 0
    for i in range(len(levels) - 1):
        if levels[i] >= levels[i+1]:
            diff = levels[i] - levels[i+1] + 1
            levels[i] -= diff
            ans += diff
    return ans
    
ans = 0
for _ in range(len(levels) - 1):
    ans += check_levels(levels)
print(ans)