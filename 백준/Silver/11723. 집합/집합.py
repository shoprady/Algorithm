import sys

def add(x):
    if x not in S: S.append(x)

def remove(x):
    if x in S: S.remove(x)

def check(x):
    if x in S: print(1)
    else: print(0)

def toggle(x):
    if x in S: S.remove(x)
    else: S.append(x)

m = int(sys.stdin.readline())
S = []
for _ in range(m):
    order = sys.stdin.readline().split()
    if order[0] == 'add': add(int(order[1]))
    elif order[0] == 'remove': remove(int(order[1]))
    elif order[0] == 'check': check(int(order[1]))
    elif order[0] == 'toggle': toggle(int(order[1]))
    elif order[0] == 'all': S = [i for i in range(1, 21)]
    elif order[0] == 'empty': S = []