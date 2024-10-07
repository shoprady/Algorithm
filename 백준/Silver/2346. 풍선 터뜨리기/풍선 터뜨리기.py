from collections import deque
n = int(input())
steps = list(map(int, input().split()))
queue = deque(range(1, n + 1))

while queue:
    i = steps[queue[0] - 1]
    print(queue.popleft(), end=' ')
    if i > 0: queue.rotate(-i + 1)
    else: queue.rotate(-i)