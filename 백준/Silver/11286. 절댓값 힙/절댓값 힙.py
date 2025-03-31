import sys
from heapq import heappush, heappop
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heappush(heap, (abs(x), x))
    else:
        try:
            print(heappop(heap)[1])
        except:
            print(0)