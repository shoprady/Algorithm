vtx = int(input())
edge = int(input())

# adj matrix 구축 후 DFS
adj = [[0 for _ in range(vtx)] for _ in range(vtx)]
for _ in range(edge):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    adj[a][b], adj[b][a] = 1, 1
    
def DFS(s, visited):
    global ans
    ans += 1
    visited[s] = True
    
    for v in range(vtx):
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(v, visited)
                
ans = -1
DFS(0, [False] * vtx)
print(ans)