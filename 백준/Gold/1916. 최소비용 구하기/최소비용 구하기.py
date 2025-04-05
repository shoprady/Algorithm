import sys, heapq
input = sys.stdin.readline
INF = float('inf')

n = int(input())
city = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b, p = map(int, input().split())
    city[a].append((b, p))

dist = [INF] * (n + 1)
x, y = map(int, input().split())
dist[x] = 0

q = []
heapq.heappush(q, (0, x))
while q:
    d, now = heapq.heappop(q)
    if dist[now] < d: continue
    for i in city[now]:
        if dist[now] + i[1] < dist[i[0]]:
            dist[i[0]] = dist[now] + i[1]
            heapq.heappush(q, (dist[i[0]], i[0]))

print(dist[y])