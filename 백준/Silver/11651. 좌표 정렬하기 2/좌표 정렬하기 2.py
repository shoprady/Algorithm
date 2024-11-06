n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))
    
points.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    point = points[i]
    for j in point:
        print(j, end=' ')
    print()