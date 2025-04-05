a, b = map(int, input().split())
c, d = map(int, input().split())

ans = []
ans.append(a/c + b/d)
ans.append(c/d + a/b)
ans.append(d/b + c/a)
ans.append(b/a + d/c)
print(ans.index(max(ans)))