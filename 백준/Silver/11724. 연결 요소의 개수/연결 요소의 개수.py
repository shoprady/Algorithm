import sys
imput = sys.stdin.readline

n, m = map(int, imput().split())
visit, count = [0] * n, 0
for _ in range(m):
    u, v = map(int, imput().split())
    if not visit[u - 1] and not visit[v - 1]:
        count += 1
        visit[u - 1] = visit[v - 1] = count
    elif visit[u - 1] != 0 and visit[v - 1] != 0 and visit[u - 1] != visit[v - 1]:
        for i in range(len(visit)):
            if visit[i] == visit[u - 1]:
                visit[i] = visit[v - 1]
    elif visit[u - 1] == 0:
        visit[u - 1] = visit[v - 1]
    elif visit[v - 1] == 0:
        visit[v - 1] = visit[u - 1]

if 0 in visit:
    print(visit.count(0) + len(set(visit)) - 1)
else: print(len(set(visit)))