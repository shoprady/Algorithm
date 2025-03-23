import sys
from collections import deque
n = int(input())
v, parent = [[] for _ in range(n)], [0] * n
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    v[a - 1].append(b - 1); v[b - 1].append(a - 1)
q = deque([0])
while q:
    node = q.popleft()
    child = v[node]
    for i in child:
        if not parent[i]:
            parent[i] = node + 1
            q.append(i)
for i in range(1, n):
    print(parent[i])