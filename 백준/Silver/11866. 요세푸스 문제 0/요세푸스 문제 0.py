from collections import deque
n, k = map(int, input().split())

people, ans = deque([i + 1 for i in range(n)]), []
for _ in range(n):
    people.rotate(-k+1)
    ans.append(people.popleft())
    
print('<', end='')
for i in ans:
    if i == ans[-1]:
        print(i, end='>')
    else:
        print(i, end=', ')