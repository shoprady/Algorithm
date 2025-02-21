from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    levels = list(map(int, input().split()))
    docs, i = deque(list(enumerate(levels))), 1
    
    while len(docs) > 0:
        max_level = max([j for i, j in docs])
        if docs[0][1] == max_level:
            doc = docs.popleft()
            if doc[0] == m:
                print(i); break
            else: i += 1
        else:
            docs.rotate(-1)