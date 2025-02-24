n, m = map(int, input().split())
hear, see = dict(), []
for _ in range(n):
    hear[input()] = 0
for _ in range(m):
    see.append(input())
    
ans = []
for i in see:
    if i in hear:
        ans.append(i)
ans.sort()
print(len(ans))
for i in ans: print(i)