def push(i, stack):
    stack.append(i)

def pop(stack):
    if len(stack) == 0:
        print(-1); return
    print(stack.pop(-1))

def size():
    print(len(stack))

def empty():
    print((len(stack) == 0) * 1)

def top():
    if len(stack) == 0:
        print(-1); return
    print(stack[-1])

n = int(input())
stack = []
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        push(int(order[1]), stack)
    elif order[0] == 'pop':
        pop(stack)
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'top':
        top()