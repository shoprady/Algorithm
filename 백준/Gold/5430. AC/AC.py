import sys
from collections import deque
imput = sys.stdin.readline

def print_arr(arr, rev):
    if rev:
        print('[', end='')
        for i in range(len(arr) - 1, 0, -1):
            print(str(arr[i]) + ',', end='')
        print(str(arr[0]) + ']')
    else:
        print('[', end='')
        for i in range(len(arr) - 1):
            print(str(arr[i]) + ',', end='')
        print(str(arr[-1]) + ']')

for _ in range(int(imput())):
    p, n, empty, rev = imput(), int(imput()), True, False
    arr = imput()[:-1].strip('[]').split(',')
    if n: q = deque(map(int, arr))
    else: q = deque([])
        
    for i in p[:-1]:
        if i == 'R':
            if rev: rev = False
            else: rev = True
        elif i == 'D' and q:
            if rev: q.pop()
            else: q.popleft()
        else:
            print('error')
            empty = False; break
            
    if empty and not q: print('[]')
    elif empty: print_arr(q, rev)
    else: continue