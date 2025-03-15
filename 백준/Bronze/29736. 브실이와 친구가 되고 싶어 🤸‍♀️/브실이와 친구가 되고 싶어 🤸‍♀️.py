a, b = map(int, input().split())
k, x = map(int, input().split())
left, right = k - x, k + x
if left > b or right < a: print('IMPOSSIBLE')
else: print(min(b, right) - max(a, left) + 1)