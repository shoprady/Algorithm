n, m = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

i, j = 0, 0
while j < m:
    if box[i] >= book[j]:
        box[i] -= book[j]
        j += 1
    else:
        i += 1
print(sum(box))