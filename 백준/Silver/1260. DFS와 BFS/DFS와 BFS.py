n, m, s = map(int, input().split())

# adj matrix, adj list 구축
adj_m = [[0 for _ in range(n)] for _ in range(n)] # adj matrix for DFS
adj_l = [[] for _ in range(n)] # adj list for BFS

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    
    adj_m[a][b], adj_m[b][a] = 1, 1
    adj_l[a].append(b)
    adj_l[b].append(a)
    
# DFS
def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True
    
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(vtx, adj, v, visited)

# BFS
def BFS(vtx, aList, s):
    n = len(vtx)
    visited = [False] * n
    q = []
    q.append(s)
    visited[s] = True
    while len(q) != 0:
        s = q.pop(0)
        print(vtx[s], end=' ')
        for v in sorted(aList[s]):
            if visited[v] == False:
                q.append(v)
                visited[v] = True

vtx = [i+1 for i in range(n)]
DFS(vtx, adj_m, s-1, [False] * len(vtx))
print()
BFS(vtx, adj_l, s-1)