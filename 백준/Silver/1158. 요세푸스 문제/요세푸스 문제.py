from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))

print('<', end='')
while len(queue) > 1:
    queue.rotate(-k+1)
    print(queue.popleft(), end=', ')
print(queue.popleft(), end='>')