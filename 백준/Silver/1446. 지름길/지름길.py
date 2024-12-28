n, d = map(int, input().split())
street = []
for _ in range(n):
    start, end, dist = map(int, input().split())
    if dist < end - start and end <= d:
        street.append([start, end, dist])
    
ans = [i for i in range(d + 1)]
street.sort(key=lambda x: x[1])

for start, end, dist in street:
    if ans[end] > ans[start] + dist:
        ans[end] = ans[start] + dist
        tmp = 1
        for i in range(end + 1, d + 1):
            ans[i] = ans[end] + tmp
            tmp += 1
            
print(ans[d])