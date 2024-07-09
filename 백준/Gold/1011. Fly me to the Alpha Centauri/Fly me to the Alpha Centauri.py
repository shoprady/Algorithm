import math
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x # 거리
    
    root = round(math.sqrt(dist))
    if root ** 2 >= dist:
        cnt = 2 * root - 1
    else:
        cnt = 2 * root
        
    print(cnt)