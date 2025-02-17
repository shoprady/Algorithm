from collections import deque

def push(i, queue):
    queue.append(i)

def pop(queue):
    if len(queue) == 0:
        print(-1); return
    print(queue.popleft())

def size():
    print(len(queue))

def empty():
    print((len(queue) == 0) * 1)

def front():
    if len(queue) == 0:
        print(-1); return
    print(queue[0])
    
def back():
    if len(queue) == 0:
        print(-1); return
    print(queue[-1])

n = int(input())
queue = deque()
for _ in range(n):
    order = input().split()
    if order[0] == 'push': push(int(order[1]), queue)
    elif order[0] == 'pop': pop(queue)
    elif order[0] == 'size': size()
    elif order[0] == 'empty': empty()
    elif order[0] == 'front': front()
    elif order[0] == 'back': back()