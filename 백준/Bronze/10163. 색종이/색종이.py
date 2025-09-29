n = int(input())
ls, arr = [], [[0] * 1001 for _ in range(1001)]
for order in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            arr[i][j] = order
flat = [x for row in arr for x in row]
for order in range(1, n+1):
    print(flat.count(order))