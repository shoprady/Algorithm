n, d = map(int, input().split())
street = []
for _ in range(n):
    start, end, dist = map(int, input().split())
    if dist < end - start and end <= d:
        street.append([start, end, dist])
    
ans = [i for i in range(d + 1)]
street.sort()

for start, end, dist in street:
    shortcut = ans[start] + dist
    if ans[end] > shortcut:
        ans[end] = min(ans[end], shortcut)
        tmp = 1
        for i in range(end + 1, d + 1):
            ans[i] = min(ans[i], ans[end] + tmp)
            tmp += 1
            
print(ans[d])