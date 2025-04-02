from collections import deque
n, k = map(int, input().split())
if n == k: print(0); exit(0)
time = [float('inf')] * 100001
time[n] = 0
q = deque([n])
while q:
    x = q.popleft()
    if 0 < x < 50001 and time[x * 2] == float('inf'):
        time[x * 2] = min(time[x * 2], time[x])
        q.append(x * 2)
    if x > 0 and time[x - 1] == float('inf'):
        time[x - 1] = min(time[x - 1], time[x] + 1)
        q.append(x - 1)
    if x < 100000 and time[x + 1] == float('inf'):
        time[x + 1] = min(time[x + 1], time[x] + 1)
        q.append(x + 1)
print(time[k])