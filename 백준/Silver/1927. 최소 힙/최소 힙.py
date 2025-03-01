import sys
import heapq
heap = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0: print(heapq.heappop(heap) if heap else 0)
    else: heapq.heappush(heap, x)